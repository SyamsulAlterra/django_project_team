from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *
 

def homepage(request):
    return render(request, 'homepage.html')

def detail(request, place_id):
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
        'testi': testi
        }
    
    return render(request, 'detail.html', context=context)


# def detail1(request):
#     tempat = Places.objects.all()
#     return render(request, 'detail.html', {'tempat':tempat})

# def detail2(request):
#     gambar = Photos.objects.all()
#     return render(request, 'detail.html', {'gambar':gambar})


# def detail3(request):
#     review = Review.objects.all() 
#     return render(request, 'detail.html', {'review':review})