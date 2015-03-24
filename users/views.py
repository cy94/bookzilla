from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
	return render(request, 'login.html')

def home(request):
	return render(request, 'home.html')