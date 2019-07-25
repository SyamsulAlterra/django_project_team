from django.shortcuts import render,redirect
from .models import *
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')

def search_result(request):
    list_places = Places.objects.all()
    return render(request, 'search_result.html', {'Places': list_places})