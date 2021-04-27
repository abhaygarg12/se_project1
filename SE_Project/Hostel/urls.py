from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='Hostel-login'),
    path('home/', views.home, name='Hostel-home'),
    #path('login/', views.login, name='user-login'),
    path('register/',views.register, name='user-register'),
]
