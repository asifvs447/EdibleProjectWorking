# from django.conf.urls import url
from django.urls import path
from .views import *

app_name='agreements'

urlpatterns =[
    path('', agree1, name='agreehtml'),
    path('signcontract/', agree1, name='agreehtml'),
]