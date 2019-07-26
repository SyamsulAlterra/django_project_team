from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *

def detail(request, place_id):

    if request.method=='POST':
        string = location_to_search(request.POST)
        if string.is_valid():
            target=string.cleaned_data['location']
            filter_places=Places.objects.all().filter(name__contains=target)
            return render(request, 'search_result.html', {'places':filter_places, 'string':string})
    else:
        string = location_to_search()

    # Generate counts of some of the main objects
    tempat = Places.objects.get(pk=place_id)
    # namaTempat=tempat.cleaned_data['name']
    gambar = Photos.objects.all().filter(place_name_id=tempat.id) 
    # place_name_id adalah variabel foreign_key
    # gambar = Photos.objects.filter(place_name__contains='Malang')
    testi = Review.objects.all().filter(place_name_id=tempat.id) 
    context = {
        'tempat': tempat,
        'gambar': gambar,
        'testi': testi,
        'string': string,
        }
    
    return render(request, 'detail.html', context=context)


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
# def result(request):
#     # request.session.pop(['string'],{})
#     if request.method=='POST':
#         string = location_to_search(request.POST)
#         if string.is_valid():
#             return render(request, 'search_result.html', {'string':string})
#     else:
#         string = location_to_search()
        
#     return render(request, 'search_result.html', {'string':string})

def location_form(request):
    if request.method=='POST':
        data = input_location(request.POST)
        string = location_to_search(request.POST)
        if data.is_valid():
            data.save()
            string = location_to_search()
            return redirect('homepage')
        elif string.is_valid():
            target=string.cleaned_data['location']
            filter_places=Places.objects.all().filter(name__contains=target)
            return render(request, 'search_result.html', {'places':filter_places, 'string':string})
    else:
        data = input_location()
        string = location_to_search()

    return render(request, 'location_form.html', {'data':data, 'string':string})


def photo_form(request):
    if request.method=='POST':
        data = input_photo(request.POST)
        string = location_to_search(request.POST)
        if data.is_valid():
            data.save()
            string = location_to_search()
            return redirect('homepage')
        elif string.is_valid():
            target=string.cleaned_data['location']
            filter_places=Places.objects.all().filter(name__contains=target)
            return render(request, 'search_result.html', {'places':filter_places, 'string':string})
    else:
        data = input_photo()
        string = location_to_search()

    return render(request, 'photo_form.html', {'data':data, 'string':string})

def review_form(request):
    if request.method=='POST':
        data = input_review(request.POST)
        string = location_to_search(request.POST)
        if data.is_valid():
            data.save()
            string = location_to_search()
            return redirect('homepage')
        elif string.is_valid():
            target=string.cleaned_data['location']
            filter_places=Places.objects.all().filter(name__contains=target)
            return render(request, 'search_result.html', {'places':filter_places, 'string':string})
    else:
        data = input_review()
        string = location_to_search()

    return render(request, 'review_form.html', {'data':data, 'string':string})