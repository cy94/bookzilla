from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as djlogin
from django.contrib.auth import logout as djlogout
from django.http import JsonResponse
# Create your views here
def login(request):
	return render(request, 'login.html')

def logout(request):
    djlogout(request)
    return render(request, 'logout.html')

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
    error = ''
    success = False
    if request.method == 'POST':
        username = request.POST.get('username', None)
        if not username:
            error = 'Please enter your username'
        elif User.objects.filter(username__exact=username).exists():
            error = 'Sorry, this username is already taken !'
        else:
            success = True

    ajax_vars = {'success': success, 'error': error}
    return JsonResponse(ajax_vars)