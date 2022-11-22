from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib import admin

# Create your models here.
# Restaurant details	
class Restaurant(models.Model):
	rname 		= models.CharField(max_length=100,blank=False)
	info	 	= models.CharField(max_length=40,blank=False)
	min_ord		= models.CharField(max_length=5,blank=False)
	location    = models.CharField(max_length=40,blank=False)

	REST_STATE_OPEN    = "Open"
	REST_STATE_CLOSE   = "Closed"
	REST_STATE_CHOICES =(
			(REST_STATE_OPEN,REST_STATE_OPEN),
			(REST_STATE_CLOSE,REST_STATE_CLOSE)
		)
	status 	= models.CharField(max_length=50,choices=REST_STATE_CHOICES,default=REST_STATE_OPEN,blank=False)
	approved = models.BooleanField(blank=False,default=True)
  

	def __str__(self):
		return self.rname