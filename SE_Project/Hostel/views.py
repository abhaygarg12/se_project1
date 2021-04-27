from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .forms import RegisterStudentForm,ComplaintForm
from .models import *

# Create your views here.

def login(request):
    return render(request, 'Hostel/login_form.html')
    
def home(request):
    return render(request, 'Hostel/home.html')

def register(request):
    form = RegisterStudentForm()
    
    if request.method == "POST":
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'Hostel/register.html', context)

def addComplaint(request):
    form = ComplaintForm()
    
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
    
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



