from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField( max_length=50)
    roll_no = models.IntegerField(primary_key=True)
    dob = models.DateField(max_length=10,help_text="format : DD-MM-YYYY", auto_now_add=True)
    mobile = models.IntegerField()
    room_no = models.CharField(max_length=5)

    def __str__(self):
        return str(self.roll_no)


class Complaint(models.Model):
    STATUS = {
			('Pending', 'Pending'),
			('Completed', 'Completed'),
    }

    rollno = models.ForeignKey(Student, on_delete = models.CASCADE)
    title = models.CharField(max_length=30, default= "")
    description = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS)   