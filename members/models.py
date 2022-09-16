from django.db import models

from events.models import *

# Create your models here.

class EventRegisteration(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.first_name + ' ' + self.last_name



class Register(models.Model):
	id = models.AutoField(primary_key=True)
	STATUS = (
			
			('YES', 'YES'),
			('MAYBE','MAYBE'),
			('NO', 'NO'),
			)

	jdevuser = models.ForeignKey(User, null=True, on_delete= models.SET_NULL,)
	event_name = models.ForeignKey(Event, null=True, on_delete= models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	Branch=models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='NO')
	count=models.IntegerField(null=True,)
	

	def __str__(self):
		return self.name
