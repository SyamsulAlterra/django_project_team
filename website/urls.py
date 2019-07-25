from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('detail/<int:place_id>', views.detail, name='detail'),
    path('result/', views.result, name='result'),#ganti sama path result
    path('location_form/', views.location_form, name='location form'),
]