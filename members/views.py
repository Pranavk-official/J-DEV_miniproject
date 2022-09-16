from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm,RegisterEventForm
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {
		'form':form,
		})

def register_event(request, pk):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = RegisterEventForm(request.POST)
			messages.success(request, ("Admins don't need to register for events"))
		else:
			form = RegisterEventForm(request.POST)
			if form.is_valid():
				#form.save()
				event = form.save(commit=False)
				event.save()
				return 	HttpResponseRedirect('/register_event?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = RegisterEventForm
		else:
			form = RegisterEventForm

		if 'submitted' in request.GET:
			submitted = True
   
	reg_participant = request.user.id
	attendee = JDEVUser.objects.filter(user=reg_participant)

	# formset = EventFormSet(instance=customer)
	formset = RegisterEventForm(initial={'event_name':Event,'jdevuser':reg_participant,'name':attendee ,'email':request.user.email})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = EventForm(request.POST)
		formset = RegisterEventForm(request.POST,)
		if formset.is_valid():
			formset.save()
	

	return render(request, 'events/register_event.html', {'form':formset, 'submitted':submitted})