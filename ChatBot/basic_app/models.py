from django.db import models

# Create your models here.
class StudentBotUser(models.Model):
	first_name=models.CharField(max_length=128)
	email=models.CharField(max_length=128)
	phone_number=models.CharField(max_length=264)