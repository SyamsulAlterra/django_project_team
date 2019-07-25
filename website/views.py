from django.shortcuts import render,redirect
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')
