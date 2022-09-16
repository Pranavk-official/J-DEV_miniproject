from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField('Venue Name', max_length=120)
	
	def __str__(self):
		return self.name


class JDEVUser(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	Bio =models.CharField(max_length=500, null=True)
	Branch=models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Event(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	approved = models.BooleanField('Aprroved', default=False)
	jdevuser = models.ForeignKey(JDEVUser, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.name

	@property
	def Days_till(self):
		today = date.today()
		days_till = self.event_date.date() - today
		days_till_stripped = str(days_till).split(",", 1)[0]
		return days_till_stripped
	
	@property
	def Is_Past(self):
		today = date.today()
		if self.event_date.date() < today:
			thing = "Past"
		else:
			thing = "Future"
		return thing