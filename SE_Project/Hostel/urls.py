from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Hostel-home'),
    path('register/', views.register, name='Hostel-register'),
]
