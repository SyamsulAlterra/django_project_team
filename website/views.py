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

    return render(request, 'homepage.html', {'string':string} )

#fungsi manggil result
def result(request):
    request.session.pop(['string'],{})
    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            return render(request, 'search_result.html', {'string':string})
    else:
        string = location_to_search()
        
    return render(request, 'search_result.html', {'string':string})

def location_form(request):
    if request.method=='POST':
        data = input_location(request.POST)
        string = location_to_search(request.POST)
        if data.is_valid():
            data.save()
            string = location_to_search()
            return redirect('homepage')
        elif string.is_valid():
            return redirect('result')
    else:
        data = input_location()
        string = location_to_search()

    return render(request, 'location_form.html', {'data':data, 'string':string})

