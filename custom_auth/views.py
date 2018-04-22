from django.shortcuts import render

# Create your views here.




from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CustomAuthMain(ListView):


    def signup(request):
        return render(request,'register/register.html')


def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'login/login.html')