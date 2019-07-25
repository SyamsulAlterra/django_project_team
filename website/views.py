from django.shortcuts import render,redirect
from .forms import *
from .models import *

def homepage(request):
    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            target=string.cleaned_data['location']
            filter_places=Places.objects.all().filter(name__contains=target)
            return render(request, 'search_result.html', {'places':filter_places, 'string':string})
    else:
        string = location_to_search()

    return render(request, 'homepage.html', {'string':string})

#fungsi manggil result
def result(request):
    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            return render(request, 'search_result.html', {'string':string})
    else:
        string = location_to_search()
        
    return render(request, 'search_result.html')
