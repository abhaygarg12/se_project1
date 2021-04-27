from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.
class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.IntegerField(validators=[MinLengthValidator(9),MaxLengthValidator(9)], primary_key=True)
    dob = models.DateField(max_length=10,help_text="format : DD-MM-YYYY")
    mobile = models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    room_no = models.CharField(max_length=5)

    def __str__(self):
        str = self.user.first_name + " " + self.user.last_name
        return str


class Complaints(models.Model):
    STATUS = {
			('Pending', 'Pending'),
			('Completed', 'Completed'),
    }

    rollno = models.ForeignKey(Students, on_delete = models.CASCADE)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS)




    