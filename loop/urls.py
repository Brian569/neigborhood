from django.urls import path, re_path
from .views import (home, logout_view,
    profile, updataProfile, business,
    my_business, create_neigborhood
     )

urlpatterns = [
    path('', home, name = 'home'),
    path('logout/', logout_view, name ='logouts'),
    re_path(r'profile/(\d+)',profile,name = 'profile'),
    path('update/', updataProfile, name = 'update'),
    path('business/', business, name = 'business'),
    re_path(r'my_business/(\d+)', my_business, name = 'my_business'),
    path('neigbor/', create_neigborhood, name = 'neigbor')
]