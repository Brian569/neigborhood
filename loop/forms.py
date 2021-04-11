from django import forms
from .models import *

class ProfileupdateForm(forms.ModelForm):
    class Meta:
        model = profileUser
        fields = ['prof_name', 'profile_pic', 'email']
        exclude = ['user', 'neighborHood']