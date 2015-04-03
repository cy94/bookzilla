from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)