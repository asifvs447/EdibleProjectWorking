# from django.conf.urls import url
from django.urls import path
from .views import *

app_name='agreements'

urlpatterns =[
    path('', EdibleHome.index, name='index'),
    path('agreements', EdibleHome.index, name='index'),
    path('agreehtml/',EdibleHome.agree1, name='agreehtml'),
]