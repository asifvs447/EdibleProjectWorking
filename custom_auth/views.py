from django.shortcuts import render

# Create your views here.




from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate

from .models import LoginPin

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CustomAuthMain(ListView):


    def signup(request):
        if request.method == 'POST':
            unique_pin = request.POST.get('unique_pin')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not password == confirm_password:
                return render(request,'register/register.html',
                              {'error': 'Passwords do not match'})
            pin_qs = LoginPin.objects.filter(key=unique_pin)
            if pin_qs.exists():
                pin = pin_qs[0]
                if pin.expired:
                    return render(request,'register/register.html',
                                  {'error': 'The PIN has expired!'})
                else:
                    first_name = request.POST.get('first_name')
                    last_name = request.POST.get('last_name')
                    number = request.POST.get('number')
                    email = request.POST.get('email')
                    if User.objects.filter(email=email).exists():
                        return render(request,'register/register.html',
                                      {'error': 'User with this email already exists!'})
                    else:
                        user = User()
                        user.username = email
                        user.email = email
                        user.set_password(password)
                        user.first_name = first_name
                        user.last_name = last_name
                        user.save()
                        pin.expired = True
                        pin.save()
                        auth.login(request, user)

                        return HttpResponseRedirect('/agreements/signcontract/')
                        
            else:
                return render(request,'register/register.html',
                              {'error': 'Invalid PIN'})

        return render(request,'register/register.html')


def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'login/login.html')