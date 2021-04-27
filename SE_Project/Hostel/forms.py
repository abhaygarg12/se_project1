from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class RegisterStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
class ComplaintForm(ModelForm):
	class Meta:
		model = Complaints
		fields = '__all__'

class StudentDetailForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
    