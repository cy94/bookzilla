from django.db import models

from django.contrib.auth.models import User

from books.models import Book

class BookRequest(models.Model):
	REQUEST_MADE = 0

	REQUEST_ACCEPTED = 1
	REQUEST_REJECTED = 2

	WITH_COURIER_TO_BORROWER = 3

	WITH_BORROWER = 4
	DONE_READING = 5

	WITH_COURIER_TO_OWNER = 6
	RETURNED = 7
	

	STATUS_CHOICES = (
		(REQUEST_MADE, 'request pending'),
		(REQUEST_ACCEPTED, 'request accepted' ),
		(REQUEST_REJECTED, 'request rejected' ),
		(WITH_COURIER_TO_BORROWER, 'being delivered to borrower' ),
		(WITH_BORROWER, 'with borrower' ),
		(DONE_READING, 'done reading' ),
		(WITH_COURIER_TO_OWNER, 'being delivered to owner' ),
		(RETURNED, 'returned' ),
	)		

	book = models.OneToOneField(Book)
	borrower = models.OneToOneField(User)
	status = models.IntegerField(default=0, choices=STATUS_CHOICES)

