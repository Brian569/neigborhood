from django.db import models
from django.contrib.auth.models import User


class NeighborHood(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    occupants = models.PositiveIntegerField()
    
    # admin = models.ForeignKey(Admin, on_delete=models.CASCADE)


class profileUser(models.Model):
    prof_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    neighborHood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


class Bussiness(models.Model):
    biz_name = models.CharField(max_length=100, blank=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, blank=True)
    profile = models.ForeignKey(profileUser, on_delete=models.CASCADE, blank=True)
    biz_email = models.EmailField(blank=True)