from django.shortcuts import render,redirect
from .forms import *

def homepage(request):
    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            return render(request, 'result.html', {'string':string})
    else:
        string = location_to_search()

    return render(request, 'homepage.html', {'string':string})

#fungsi manggil result
def result(request):
    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            return render(request, 'result.html', {'string':string})
    else:
        string = location_to_search()
        
    return render(request, 'result.html')
