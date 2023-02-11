from django.db import models

# Create your models here.
class Marks(models.Model):
    Std_name = models.CharField(max_length=200)
    phy = models.PositiveIntegerField()
    chem = models.PositiveIntegerField()
    bio = models.PositiveIntegerField()
    math = models.PositiveIntegerField()
    eng=models.PositiveIntegerField()
    kannada = models.PositiveIntegerField()
