from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .forms import *

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .decoraters import *

# Create your views here.


@unauthenticated_user
def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        roll_no = request.POST.get("roll_no")
        room_no = request.POST.get("room_no")
        mobile = request.POST.get("mobile")
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already registered")
                return redirect('user-register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('user-register')
            elif Student.objects.filter(roll_no=roll_no).exists():
                messages.error(request, "Roll number already registered")
                return redirect('user-register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created for " + username)
                group = Group.objects.get(name="student")
                user.groups.add(group)

                student = Student.objects.create(
                    user=user, full_name=full_name, room_no=room_no, roll_no=roll_no, mobile=mobile, dob=dob)
                # student.save()

                return redirect('user-login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('user-register')

    return render(request, 'Hostel/register_form.html')


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
            messages.info(request, 'Invalid Credentials')

    context = {}
    return render(request, 'Hostel/login_form.html', context)


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

    context = {'form': form}
    return render(request, 'Hostel/Addnewcomplaint.html', context)


'''
#original functions
def new_complaint(request, pk):
    student = Students.objects.all(id = pk)
    form = ComplaintForm(initial={'student':student})

    if request.method == 'POST':
		form = ComplaintForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home/')

	context = {'form':form}
	return render(request, 'Hostel/new_complaint.html', context)
    
    
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
    return render(request, 'Hostel/register_form.html')'''
