from django import forms
from .models import *

class ProfileupdateForm(forms.ModelForm):
    class Meta:
        model = profileUser
        fields = ['profile_name', 'profile_pic', 'email', 'location', 'bio']
        exclude = ['user']


class BussinessForm(forms.ModelForm):
    class Meta:
        model = Bussiness
        fields = ['business_name', 'business_email', 'phone_number', 'neighborhood', 'business_photo', 'details']
        exclude = ['owner']

class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        fields = ['name', 'location', 'image']
        exclude = ['resider']

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'picture']
        exclude = ['owner']

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ['name', 'email', 'picture', 'about', 'neighborhood', 'phone_number']


class PoliceForm(forms.ModelForm):
    class Meta:
        model = Police
        fields = ['name',  'email', 'image', 'neigborhood', 'phone_number', 'about']