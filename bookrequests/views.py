from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# models
from books.models import Book
from .models import BookRequest

@login_required
def lent_index(request):
	user = request.user
	requests = BookRequest.objects.all()

	# get requests where the owner is 'user'
	my_lent = (r for r in requests if r.book.owner == user)

	print my_lent

	return render(request,
				'bookrequests/lent_index.html', 
				{
					'requests': my_lent
				})

@login_required
def borrowed_index(request):
	user = request.user
	requests = BookRequest.objects.all()

	# get requests where the borrower is 'user'
	my_borrowed = (r for r in requests 
						if r.borrower == user)

	print my_borrowed

	return render(request,
				'bookrequests/borrowed_index.html', 
				{
					'requests': my_borrowed
				})

