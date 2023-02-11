from django.db import models #BY DEAFULT

# Create your models here.

class Student_details(models.Model):
    # creating a student id variabel and input conditions
    std_name = models.CharField(max_length=260)
    std_age = models.PositiveIntegerField()
    std_gender = models.CharField(max_length=200)
    std_phone = models.PositiveSmallIntegerField(unique=True)
    std_email = models.EmailField(max_length=260, unique=True)


