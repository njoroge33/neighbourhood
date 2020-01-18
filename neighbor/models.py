from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)
    total_occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def create_neighborhood():
        self.save()

    def delete_neighborhood():
        self.delete()
