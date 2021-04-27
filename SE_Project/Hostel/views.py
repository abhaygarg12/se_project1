from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .decoraters import *

# Create your views here.

@unauthenticated_user
def register(request):
    form = RegisterStudentForm()

    if request.method == "POST":
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            group = Group.objects.get(name = "student")
            user.groups.add(group)

            return redirect('student-details')
            #return redirect('Hostel-home')
    
    context = {'form':form}
    return render(request, 'Hostel/register.html', context)

@unauthenticated_user
#@registered_user
def student_details(request):
    form = StudentDetailForm()

    if request.method == "POST":
        form = StudentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hostel-home')
    
    context = {'form':form}
    return render(request, 'Hostel/register1.html', context)

@unauthenticated_user
def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Hostel-home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
        
    context={}
    return render(request, 'Hostel/login_form.html',context)

def logout_user(request):
    logout(request)
    return redirect('user-login')
    
@login_required(login_url='user-login')
def home(request):
    return render(request, 'Hostel/home.html')

@login_required(login_url='user-login')
def new_complaint(request):
    form = ComplaintForm()

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Hostel-home')
    
    context = {'form':form}
    return render(request, 'Hostel/register.html', context)


'''
#original function
def new_complaint(request, pk):
    student = Students.objects.all(id = pk)
    form = ComplaintForm(initial={'student':student})

    if request.method == 'POST':
		form = ComplaintForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home/')

	context = {'form':form}
	return render(request, 'Hostel/new_complaint.html', context)'''
