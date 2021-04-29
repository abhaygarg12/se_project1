from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home, name='Hostel-home'),
    path('student_home/', views.student_home, name='student-home'),
    path('caretaker_home/', views.caretaker_home, name='caretaker-home'),
    path('warden_home', views.warden_home, name='warden-home'),

    path('login/', views.login_page, name='user-login'),
    path('logout/', views.logout_user, name='user-logout'),
    path('register/', views.register, name='user-register'),

    path('update_details/',views.update_details, name='update-datails'),
    path('change_pass/',views.change_pass, name='change-pass'),
    path('delete_student/<str:pk>',views.delete_student, name='delete-student'),

    path('new_complaint/', views.new_complaint, name='new-complaint'),

]

