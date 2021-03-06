from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_home, name='Hostel-home'),
    path('student_home/', views.student_home, name='student-home'),
    path('contact/', views.contact_page, name='contact-page'),

    path('caretaker_home/', views.caretaker_home, name='caretaker-home'),
    path('caretaker_home/students', views.caretaker_students,
         name='caretaker-students'),

    path('warden_home', views.warden_home, name='warden-home'),
    path('warden_home/students', views.warden_students, name='warden-students'),
    path('warden_home/caretakers', views.warden_caretakers,
         name='warden-caretakers'),
    path('warden_home/add_caretaker',
         views.warden_addcaretaker, name='warden-addcaretaker'),

    path('login/', views.login_user, name='user-login'),
    path('logout/', views.logout_user, name='user-logout'),
    path('register/student', views.register_student, name='user-register'),
    path('register/caretaker', views.register_caretaker, name='caretaker-register'),

    path('update_details/', views.update_details, name='update-details'),
    path('change_pass/', views.change_pass, name='change-pass'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete-student'),
    path('student_pages/', views.student_page, name='student-pages'),
    path('add_student/', views.add_student, name='add-student'),

    path('add_caretaker/<str:pk>/', views.add_caretaker, name='add-caretaker'),
    path('remove_caretaker/<str:pk>',
         views.remove_caretaker, name='remove-caretaker'),

    # CRUD PART
    path('add_complaint/', views.add_complaint, name='add-complaint'),
    path('update_complaint/<str:pk>/', views.update_complaint, name='update-complaint'),
    path('delete_complaint/<str:pk>/', views.delete_complaint, name="delete-complaint"),
    path('set_status/<str:pk>/', views.set_status, name='set-status'),
    path('complaint_details/<str:pk>/', views.complaint_details, name="complaint-details"),


    # reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(
         template_name="Hostel/password_reset.html"),
         name="reset_password"),
         
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
         template_name="Hostel/password_reset_done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name="Hostel/password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name="Hostel/password_reset_complete.html"),
         name='password_reset_complete'),

]
