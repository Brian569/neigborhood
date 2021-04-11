from django.urls import path, re_path
from .views import (home, logout_view,
    profile, updataProfile
     )

urlpatterns = [
    path('', home, name = 'home'),
    path('logout/', logout_view, name ='logouts'),
    re_path(r'profile/(\d+)',profile,name = 'profile'),
    path('update/', updataProfile, name = 'update'),
]