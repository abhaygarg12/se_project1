from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from .models import *


class RegisterStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

