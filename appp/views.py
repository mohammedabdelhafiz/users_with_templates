from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    context={
        'users':users.objects.all()
    }
    return render(request,'home.html', context)
 

def rout(request):
    sign_up_form(request)
    return redirect('/')


def false(request):
    return render(request,'wrong.html')

