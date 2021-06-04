from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    room_no = models.CharField(max_length=5)

    def __str__(self):
        return str(self.user.username)


class Complaint(models.Model):
    STATUS = {
			('Pending', 'Pending'),
			('Completed', 'Completed'),
    }

    name = models.ForeignKey(Student, on_delete = models.CASCADE)
    title = models.CharField(max_length=50, default= "")
    description = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    def __str__(self):
        return self.title

class Admin(models.Model):
    POST = {
			('Caretaker', 'Caretaker'),
			('Warden', 'Warden'),
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    post = models.CharField(max_length=10, choices=POST, default='Caretaker')
    def __str__(self):
        return str(self.user.username)
