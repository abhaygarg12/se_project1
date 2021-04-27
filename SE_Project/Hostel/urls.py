from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='Hostel-login'),
    path('home/', views.home, name='Hostel-home'),
    #path('register/', include('users.urls')),
    path('register/',views.register, name='users-register'),
]
