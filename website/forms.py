from django import forms

#form buat search
class location_to_search(forms.Form):
    location=forms.CharField(max_length=200)