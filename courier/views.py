from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'courier/index.html')

def login(request):
	return render(request, 'courier/index.html')

def logout(request):
	return render(request, 'courier/index.html')