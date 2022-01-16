from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200, null=True)
	aadhar = models.IntegerField(blank=False)
	pan = models.IntegerField(blank=False)
	address = models.CharField(max_length=350, blank=True)
	profile = models.ImageField(upload_to='upload/main/img/', default='upload/main/img/profile_default.jpg', blank=True)

	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
	# kyc status 
	status = models.BooleanField(default=False)
	# source 
	source = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name