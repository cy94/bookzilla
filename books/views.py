from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
@login_required
def index(request):
	print "books index"
	return render(request, 'index.html')