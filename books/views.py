from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book

from .forms import EditBookForm

# Create your views here.
@login_required
def index(request):
	user = request.user
	book_list = user.books.all()

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

@login_required
def edit_book(request):
	if request.method == 'POST':
		form = EditBookForm(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			author = form.cleaned_data['author']

			print title, author
			
		return HttpResponseRedirect(reverse("users:books:index"))
	else:
		form = EditBookForm()
		return render(request, 
					'books/edit_books.html',{
						'form': form
					})



