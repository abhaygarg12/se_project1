from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
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
def register_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        room_no = request.POST.get("room_no")
        mobile = request.POST.get("mobile")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if len(username) != 9 or username[:2] != '10':
            messages.error(request, "Roll number should be registered in Thapar university")
            return redirect('user-register')
        else:
            pass
                    
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Roll number already registered")
                return redirect('user-register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('user-register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Account created for " + username)
                group = Group.objects.get(name="student")
                user.groups.add(group)
                student = Student.objects.create(
                    user=user, room_no=room_no, mobile=mobile)
                return redirect('user-login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('user-register')

    return render(request, 'Hostel/register_student.html')


@unauthenticated_user
def register_caretaker(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        mobile = request.POST.get("mobile")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Email already registered")
                return redirect('caretaker-register')
            elif User.objects.filter(email=username).exists():
                messages.error(request, "Email already registered")
                return redirect('caretaker-register')
            else:
                user = User.objects.create_user(
                    username=username, email=username, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Account created for " + username)
                Admin.objects.create(user=user, mobile=mobile)
                return render(request, 'Hostel/application_review.html')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('caretaker-register')

    return render(request, 'Hostel/register_caretaker.html')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Hostel-home')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'Hostel/login_form.html')


def logout_user(request):
    logout(request)
    return redirect('user-login')


@login_required(login_url='user-login')
@home_pages
def user_home(request):
    pass


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['caretaker', 'warden'])
@student_pages
def student_page(request):
    pass


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['student'])
def student_home(request):
    user = User.objects.get(username=request.user)
    student = Student.objects.get(user=user)
    complaints = list(Complaint.objects.filter(name=student).order_by('date_created'))
    complaints.reverse()
    context = {'complaints': complaints}
    return render(request, 'Hostel/student_home.html', context)

@login_required(login_url='user-login')
def contact_page(request):
    admin = Admin.objects.all()
    caretakers=[]
    wardens=[]
    for ad in admin:
        if ad.post == 'Caretaker':
            if ad.user.groups.exists():
                caretakers.append(ad)
        else:
            wardens.append(ad)
    print(wardens)
    context={'caretakers':caretakers, 'wardens':wardens}
    return render(request, 'Hostel/contact_page.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['caretaker'])
def caretaker_home(request):
    if request.method == "POST":
        category = request.POST.get("filter")
        if category == '0':
            complaints = list(Complaint.objects.all().order_by('date_created'))
            complaints.reverse()
        else:
            complaints = list(Complaint.objects.filter(location=category).order_by('date_created'))
            complaints.reverse()
    else:
        complaints = list(Complaint.objects.all().order_by('date_created'))
        complaints.reverse()
    
    c = Complaint.objects.all()
    filter = []
    for i in c:
        l = i.location
        if l in filter:
            pass
        else:
            filter.append(l)
    context = {'complaints': complaints, 'filters':filter}
    return render(request, 'Hostel/caretaker_home.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['caretaker'])
def caretaker_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'Hostel/caretaker_homes.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def warden_home(request):
    if request.method == "POST":
        category = request.POST.get("filter")
        if category == '0':
            complaints = list(Complaint.objects.all().order_by('date_created'))
            complaints.reverse()
        else:
            complaints = list(Complaint.objects.filter(location=category).order_by('date_created'))
            complaints.reverse()
    else:
        complaints = list(Complaint.objects.all().order_by('date_created'))
        complaints.reverse()
    
    c = Complaint.objects.all()
    filter = []
    for i in c:
        l = i.location
        if l in filter:
            pass
        else:
            filter.append(l)
    context = {'complaints': complaints, 'filters':filter}
    return render(request, 'Hostel/warden_home.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def warden_addcaretaker(request):
    admin = list(Admin.objects.all())
    caretakers = list(Admin.objects.none())
    for caretaker in admin:
        if caretaker.user.groups.exists():
            pass
        else:
            caretakers.append(caretaker)
    context = {'caretakers': caretakers}
    return render(request, 'Hostel/warden_homeaddct.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def warden_caretakers(request):
    admin = Admin.objects.all()
    caretakers = []
    for caretaker in admin:
        if caretaker.user.groups.exists():
            group = caretaker.user.groups.all()[0].name
            if group == 'caretaker':
                caretakers.append(caretaker)
    context = {'caretakers': caretakers}
    return render(request, 'Hostel/warden_homect.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def warden_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'Hostel/warden_homes.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['student'])
def update_details(request):
    user = User.objects.get(username=request.user)
    student = Student.objects.get(user=user)

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        room_no = request.POST.get("room_no")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")

        if user.check_password(password):
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            student.mobile = mobile
            user.email = email
            student.room_no = room_no
            user.save()
            student.save()
            login(request, user)
            return redirect('Hostel-home')
            messages.success(request, "User details updated!!")

        else:
            messages.error(request, "Enter the correct password to update details")
            return redirect('update-details')

    context = {'student': student}
    return render(request, 'Hostel/update_details.html', context)


@login_required(login_url='user-login')
def change_pass(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user = User.objects.get(username=request.user)
        if user.check_password(password):
            if password1 == password2:
                user.set_password(password1)
                user.save()
                login(request, user)
                messages.success(request, "Password changed successfully!!")
                return redirect('Hostel-home')
            else:
                messages.error(request, "Passwords do not match")
                return redirect('change-pass')
        else:
            messages.error(request, "Enter the correct old password")
            return redirect('change-pass')

    return render(request, 'Hostel/change_pass.html')


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['caretaker', 'warden'])
def delete_student(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        student = Student.objects.get(user=user)
        student.delete()
        user.delete()
        messages.info(request, 'Student deleted successfully!!')
        return redirect('student-pages')
    return render(request, 'Hostel/confirm_delete.html')


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['caretaker', 'warden'])
def add_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        room_no = request.POST.get("room_no")
        mobile = request.POST.get("mobile")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Roll number already registered")
                return redirect('add-student')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('add-student')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Account created for " + username)
                group = Group.objects.get(name="student")
                user.groups.add(group)
                student = Student.objects.create(
                    user=user, room_no=room_no, mobile=mobile)
                messages.success(request, "Student added successfully!!")
                return redirect('Hostel-home')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('add-student')

    return render(request, 'Hostel/add_student.html')


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def add_caretaker(request, pk):
    caretaker = Admin.objects.get(id=pk)
    user = caretaker.user
    user.groups.clear()
    group = Group.objects.get(name="caretaker")
    user.groups.add(group)
    user.save()
    messages.success(request, "Caretaker added successfully!!")
    return redirect('warden-addcaretaker')


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden'])
def remove_caretaker(request, pk):
    if request.method == "POST":
        caretaker = Admin.objects.get(id=pk)
        user = caretaker.user
        user.delete()
        messages.info(request, "Caretaker removed successfully!!")
        return redirect('warden-caretakers')
    return render(request, 'Hostel/confirm_delete.html')


@login_required(login_url='user-login')
def add_complaint(request):
    if request.method == 'POST':
        user = request.user
        name = Student.objects.get(user=user)
        title = request.POST.get("title")
        description = request.POST.get("description")
        location = request.POST.get("location")
        complaint = Complaint.objects.create(title=title, description=description, location=location, name=name)
        messages.success(request, "Complaint added successfully!!")
        return redirect('Hostel-home')
    c = Complaint._meta.get_field('location').choices
    category = []
    for i in c:
        l = i[0]
        if l in category:
            pass
        elif l == "Other":
            pass
        else:
            category.append(l)
    category.append("Other")
    return render(request, 'Hostel/add_complaint.html', {'category':category})


@login_required(login_url='user-login')
def update_complaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        location = request.POST.get("location")
        complaint.title = title
        complaint.description = description
        complaint.location = location
        complaint.save()
        messages.success(request, "Complaint updated successfully!!")
        return redirect('Hostel-home')
    c = Complaint._meta.get_field('location').choices
    category = []
    for i in c:
        l = i[0]
        if l in category:
            pass
        elif l == "Other":
            pass
        else:
            category.append(l)
    category.append("Other")
    context = {'complaint': complaint, 'category':category}
    return render(request, 'Hostel/update_complaint.html', context)


@login_required(login_url='user-login')
def delete_complaint(request, pk):
    if request.method == 'POST':
        complaint = Complaint.objects.get(id=pk)
        complaint.delete()
        messages.info(request, "Complaint deleted successfully!!")
        return redirect('Hostel-home')
    return render(request, 'Hostel/confirm_delete.html')

@login_required(login_url='user-login')
def complaint_details(request, pk):
    complaint = Complaint.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('Hostel-home')
    context={'complaint':complaint}
    return render(request, 'Hostel/complaint_details.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['warden','caretaker'])
def set_status(request, pk):
    complaint = Complaint.objects.get(id=pk)
    if complaint.status == 'Pending':
        complaint.status = 'Completed'
    elif complaint.status == 'Completed':
        complaint.status = 'Pending'

    complaint.save()
    return redirect('Hostel-home')
