from django.db import models
from django import forms
from .models import *

#form buat search
class location_to_search(forms.Form):
    location=forms.CharField(max_length=200)

class input_location(forms.ModelForm):
    class Meta:
        model=Places
        fields=('name', 'description', 'maps')

class input_photo(forms.ModelForm):
    class Meta:
        model=Photos
        fields=('place_name','pic_url')

class input_review(forms.ModelForm):
    class Meta:
        model=Review
        fields=('place_name', 'review')