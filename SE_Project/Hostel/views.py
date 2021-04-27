from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'Hostel/login_form.html')
    
def home(request):
<<<<<<< HEAD
    # return HttpResponse('Complaint system')
    return render(request, 'Hostel/index.html')


def register(request):
    # return HttpResponse('Complaint system')
    return render(request, 'Hostel/home.html')
=======
    return render(request, 'Hostel/login_form.html')
>>>>>>> 3de994b3e5c8a2f80e282f9faf6ec6be3c2e6c88
