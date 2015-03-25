from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate
from django.contrib.auth import login as djlogin

# Create your views here
def login(request):
	return render(request, 'login.html')

def login_validate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        djlogin(request, user)
        return HttpResponseRedirect(reverse('users:home'))
    else:
        return HttpResponseRedirect(reverse('users:login'))

def home(request):
	return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def register_validate(request):
    # if correct
    # return HttpResponseRedirect(reverse('users:home'))
    # else
    return HttpResponseRedirect(reverse('users:register'))