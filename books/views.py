from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
@login_required
def index(request):
	user = request.user
	book_list = user.books.all()
	print book_list

	return render(request, 'books/index.html', {
			'book_list': book_list
		})

