from django.db import models

from django.contrib.auth.models import User

from books.models import Book

class BookRequest(models.Model):
	WITH_OWNER = 0
	REQUEST_ACCEPTED = 1
	WITH_COURIER_TO_BORROWER = 2
	WITH_BORROWER = 3
	DONE_READING = 4
	WITH_COURIER_TO_OWNER = 5
	RETURNED = 6
	REQUEST_REJECTED = 7

	STATUS_CHOICES = (
		(WITH_OWNER , 'with owner')
		(ACCEPTED , 'accepted')
		(WITH_COURIER_TO_BORROWER , '')
		(WITH_BORROWER , '')
		(DONE_READING , '')
		(WITH_COURIER_TO_OWNER , '')
		(RETURNED , '')
	)		

	book = models.OneToOneField(Book)
	borrower = models.OneToOneField(User)
	status = models.IntegerField(default=0, choices=STATUS_CHOICES)

