from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as djlogin
from django.contrib.auth import logout as djlogout

from .forms import LoginForm

from .misc import is_member

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None and is_member(user, 'Couriers'):
				djlogin(request, user)
				return HttpResponseRedirect(reverse('courier:home'))
			else:
				messages.error(request,
		     	'The username or password you entered is incorrect')

	form = LoginForm()
	return render(request, 'courier/index.html',
				{
					'form': form
				})

@login_required(login_url='/courier/login')
def home(request):
	return render(request, 'courier/home.html')

@login_required(login_url='/courier/login')
def logout(request):
	djlogout(request)
	return HttpResponseRedirect(reverse('courier:login'))