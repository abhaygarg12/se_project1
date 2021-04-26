from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('Complaint system')
    return render(request, 'Hostel/index.html')


def register(request):
    # return HttpResponse('Complaint system')
    return render(request, 'Hostel/registerform.html')
