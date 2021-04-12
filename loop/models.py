from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class NeighborHood(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = CloudinaryField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    resider = models.ForeignKey('profileUser', on_delete=models.CASCADE, null= True)
    
    def __str__(self):
        return self.name

    def delete_neib(self):
        self.delete()

    def save_neib(self):
        self.name


class Bussiness(models.Model):
    business_photo = CloudinaryField(blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    business_email = models.EmailField(blank=True)
    details = models.TextField(blank=True)
    phone_number = models.IntegerField( blank=True, default='add your phone number')

    def save_biz(self):
        self.save()

    def __str__(self):
        return self.business_name

    def get_biz(self):
        business = Bussiness.objects.all()
        return business

class profileUser(models.Model):
    profile_name = models.CharField(max_length=100, blank=True)
    profile_pic = CloudinaryField('image', blank=True)
    email = models.EmailField(blank=True)
    bio = models.CharField(max_length=1000, blank=True)

    location = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,blank=True,  null=True)
    business = models.ForeignKey(Bussiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def save_user(self):

        self.save()

    def __str__(self):
        return self.profile_name

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    picture = CloudinaryField( 'image')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Health(models.Model):
    name = models.CharField(max_length=100, blank=True)
    picture = CloudinaryField('image', blank=True)
    email = models.EmailField(blank=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
    phone_number = models.IntegerField( blank=True)
    about = models.TextField(blank=True)


    def __str__(self):
        return self.name

class Police(models.Model):
    image = CloudinaryField('image', blank=True)
    name = models.CharField(max_length=100, blank=True)
    neigborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null= True)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(default=999)
    about = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

