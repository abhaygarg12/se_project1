from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'Hostel/login_form.html')
    
def home(request):
    return render(request, 'Hostel/login_form.html')