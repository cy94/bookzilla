from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')