from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)
    total_occupants = models.CharField(max_length = 50)
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    

