from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.
class Students(models.Model):
    roll_no = models.IntegerField(validators=[MinLengthValidator(9),MaxLengthValidator(9)], primary_key=True)
    student_name = models.CharField(max_length=30)
    dob = models.DateField(max_length=10,help_text="format : DD-MM-YYYY")
    mobile = models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    room_no = models.CharField(max_length=5)

    def __str__(self):
        return self.student_name

class Complaints(models.Model):
    rollno = models.ForeignKey(Students, on_delete = models.CASCADE)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=10)


    