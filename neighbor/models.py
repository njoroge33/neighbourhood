from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)
    total_occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    health_contacts = models.CharField(max_length = 50)
    police_contacts = models.CharField(max_length = 50)
    
    def create_neighborhood():
        self.save()

    def delete_neighborhood():
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length = 100)
    profile_photo = models.ImageField(upload_to = 'posts/')
    national_id = models.CharField(max_length = 9)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null=True, blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def updateProfile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.created(user=kwargs['instance'])

            post_save.connect(Profile, sender=User)

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
    bussiness_email = models.CharField(max_length = 100)
