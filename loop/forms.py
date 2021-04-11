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
        fields = ['business_name', 'business_email', 'neighborhood']
        exclude = ['owner']

class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        fields = ['name', 'location']
        exclude = ['resider']
