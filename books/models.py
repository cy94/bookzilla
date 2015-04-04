from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	owner = models.ForeignKey(User, related_name='books')
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)

	def __str__(self):
		return "%s by %s" %(self.title, self.author)
