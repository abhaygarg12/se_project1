from django.db import models
from users.models import Students

# Create your models here.
class Complaints(models.Model):
    rollno = models.ForeignKey(Students, on_delete = models.CASCADE)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=10)
    