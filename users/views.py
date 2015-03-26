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
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')  
        fname    = request.POST.get('firstName')  
        lname    = request.POST.get('lastName')  
        address  = request.POST.get('address')  
        dob      = request.POST.get('dob')  
        password = request.POST.get('password')  

        inputs = (username, email, 
                fname, lname, address,
                address, dob, password)   

        if User.objects.filter(username__exact=username).exists():
            message = 'name_taken'

        elif User.objects.filter(email__exact=email).exists():
            message = 'email_taken'
        
        if not message:
            # create a new user 
            new_user = User.objects.create_user(
                            username=username, email=email, password=password,
                            first_name=fname,
                            last_name=lname
                        )

            message = "no_error"
            # create UserInfo object
        return HttpResponse(message) 
            
            
    
                        



        

