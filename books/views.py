from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book

# Create your views here.
@login_required
def index(request):
	user = request.user
	book_list = user.books.all()
	print book_list

	return render(request, 'books/index.html', {
			'book_list': book_list
		})

@login_required
def add_book(request):
	if request.method == 'POST':
		user = request.user
		title = request.POST.get("title")
		author = request.POST.get("author")

		new_book = Book(owner = user, title = title, author = author)
		new_book.save()

		return HttpResponseRedirect(reverse("users:books:index"))
	else:
		return render(request, 'books/add_book.html')



