from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterStudentForm

# Create your views here.

def login(request):
    return render(request, 'Hostel/login_form.html')
    
def home(request):
    return render(request, 'Hostel/login_form.html')

def register(request):
    form = RegisterStudentForm()
    
    if request.method == "POST":
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'Hostel/register.html', context)