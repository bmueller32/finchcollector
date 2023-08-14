from django.db import models

# Create your models here.
class Finch(models.Model):
	# define the column names, and the dataypes in each row
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
	# CharField, TextField, IntegerField - these are called Field Types in Django 