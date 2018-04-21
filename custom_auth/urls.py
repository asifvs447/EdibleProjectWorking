# from django.conf.urls import url
from django.urls import path
from .views import *

app_name='custom_auth'

urlpatterns =[
    path('signup/', CustomAuthMain.signup, name='employeeSignup'),
    ]