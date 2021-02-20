"""
Definition of urls for VirgisPlants.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants, name='plants'),
    path('gallery/', views.gallery, name='gallery'),
    path('buy/', views.buy, name='buy'),
]
