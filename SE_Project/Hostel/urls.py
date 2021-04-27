from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Hostel-home'),
    path('login/', views.login_page, name='user-login'),
    path('logout/', views.logout_user, name='user-logout'),
    path('register/', views.register, name='user-register'),
    path('register/enter_details', views.student_details, name='student-details'),
    path('new_complaint/', views.new_complaint, name='new-complaint'),

]

