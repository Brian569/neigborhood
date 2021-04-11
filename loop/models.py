from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class NeighborHood(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    occupants = models.PositiveIntegerField()
    
    # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class profileUser(models.Model):
    prof_name = models.CharField(max_length=100, blank=True)
    profile_pic = CloudinaryField('image', blank=True)
    email = models.EmailField(blank=True)

    neighborHood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, blank=True, null=True)
    business = models.ForeignKey('Bussiness', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def save_user(self):
        self.save()

class Bussiness(models.Model):
    biz_name = models.CharField(max_length=100, blank=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(profileUser, on_delete=models.CASCADE, blank=True, null=True)
    biz_email = models.EmailField(blank=True)