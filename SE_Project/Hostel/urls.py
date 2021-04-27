from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Hostel-login'),
    path('home/', views.home, name='Hostel-home'),
    path('register/', views.register, name='user-register'),
    path('new_complaint/', views.new_complaint, name='new-complaint'),
]
