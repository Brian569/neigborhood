from django.urls import path, re_path
from .views import (home, logout_view,
    profile, updataProfile, business,
    my_business, create_neigborhood, posts,
    create_post, single_hood, create_health,
    centers, police, create_police, about,
    single_business, single_neighbor,
     )

urlpatterns = [
    path('', about, name = 'about'),
    path('home/', home, name = 'home'),
    path('logout/', logout_view, name ='logouts'),
    re_path(r'profile/(\d+)',profile,name = 'profile'),
    path('update/', updataProfile, name = 'update'),
    path('business/', business, name = 'business'),
    re_path(r'my_business/(\d+)', my_business, name = 'my_business'),
    path('neigbor/', create_neigborhood, name = 'neigbor'),
    path('posts/', posts, name = 'posts'),
    path('create_post/', create_post, name = 'create_post'),    
    re_path(r'single_hood/(\d+)', single_hood, name = 'single_hood'),
    path('create_health/', create_health, name = 'create_health'),
    path('centers/', centers, name = 'centers'), 
    path('police/', police, name = 'police'),
    path('create_police/', create_police, name = 'create_police'),
    re_path(r'single_business/(\d+)', single_business, name = 'single_business'),
    re_path(r'single_neighbor/(\d+)', single_neighbor, name = 'single_neighbor'),
]