from django.shortcuts import render, get_object_or_404

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect

from books.models import Book
from bookrequests.models import BookRequest

from .forms import EditBookForm

# for search
from django.db.models import Q

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

		messages.success(request,
				'Added your book successfully'
				)

		return HttpResponseRedirect(reverse("users:books:index"))
	else:
		return render(request, 'books/add_book.html')

@login_required
def edit_book(request, book_id):
	# the decorator makes sure there is a user
	user = request.user

	# book not found - 404 or error message ?
	book = get_object_or_404(Book, pk=book_id)

	# book does not belong to user - error
	if book not in user.books.all():
		return HttpResponseRedirect(reverse("users:home"))

	# form submitted - update the model
	if request.method == 'POST':
		form = EditBookForm(request.POST)

		if form.is_valid():
			book.title = form.cleaned_data['title']
			book.author = form.cleaned_data['author']
			book.save()

			messages.success(request,
				'Updated your book successfully'
				)

		return HttpResponseRedirect(reverse("users:books:index"))
		
	# display the form
	else:
		form = EditBookForm({
				'title': book.title,
				'author': book.author
			})

		return render(request, 
					'books/edit_book.html',{
						'form': form,
						'book_id': book_id
					})

@login_required
def delete(request, id):
    book = get_object_or_404(Book, pk=id)

    if (book.owner == request.user):
    	book.delete()
    	messages.success(request, 'Deleted your book successfully')
    else:
    	messages.warning(request, 'Could not delete this book')

    return HttpResponseRedirect(reverse("users:books:index"))

@login_required
def search(request):
	if request.method == 'POST':
		query_string = request.POST.get('query')
		results = Book.objects.filter(
				Q(title__icontains=query_string) |
				Q(author__icontains=query_string)
			)

		return render(request, 
						'books/search.html', {
						'results': results
					})
	else:
		return HttpResponseRedirect(reverse("users:books:index"))		

@login_required
def make_request(request, id):
	book_obj = get_object_or_404(Book, pk=id)
	new_request = BookRequest(book = book_obj, borrower = request.user,
							 status = BookRequest.REQUEST_MADE)
	new_request.save()
	messages.success(request, 'You have successfully requested this book')

	return HttpResponseRedirect(reverse("users:books:index"))