from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import logout


@login_required
def home(request):
    business = Bussiness.objects.all()
    profiles = profileUser.objects.all()
    neighborhoods = NeighborHood.objects.all()

    context = {'business': business, 'profiles': profiles, 'neighborhoods': neighborhoods}

    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request, prof_id):
    user = User.objects.get(pk = prof_id)
    
    profile = profileUser.objects.filter(user=prof_id)
    business = Bussiness.objects.filter(owner=prof_id)
    neighborhood = NeighborHood.objects.filter(resider=prof_id)

    return render(request, 'profile.html', {"profile": profile, 'business' : business, 'neighborhood' : neighborhood})


@login_required
def single_hood(request, neib_id):
    hood = NeighborHood.objects.filter(pk  = neib_id)
    business = Bussiness.objects.filter(neighborhood=neib_id)

    return render(request, 'single_hood.html', {'hoods' : hood, 'business' : business})


@login_required
def updataProfile(request):
    current_user = request.user

    if request.method == 'POST':
        if profileUser.objects.filter(user_id = current_user).exists():
            form = ProfileupdateForm(request.POST, request.FILES, instance= profileUser.objects.get(user_id = current_user))

        else:
            form = ProfileupdateForm(request.POST, request.FILES)
        
        if form.is_valid():
            user_prof = form.save(commit=False)
            user_prof.user = current_user
            user_prof.save()

        return redirect('profile', current_user.id)
    
    else:
        if profileUser.objects.filter(user_id = current_user).exists():
            form = ProfileupdateForm(instance=profileUser.objects.get(user_id = current_user))

        else:
            form = ProfileupdateForm()
    
    return render(request, 'update.html', {'form' : form})

@login_required
def my_business(request, biz_id):
    business = Bussiness.objects.filter(owner=biz_id)
    hood = NeighborHood.objects.filter(resider=biz_id)

    return render(request, 'my_business.html', {'business' : business, 'hood': hood})


@login_required
def business(request):
    current_user = request.user

    profile = profileUser.objects.get(user=current_user)

    if request.method == 'POST':
        form = BussinessForm(request.POST)

        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.save()

            return redirect('profile', current_user.id)
        
    else:
        form = BussinessForm()
    
    return render(request, 'business.html', {'form' : form})


@login_required
def create_neigborhood(request):

    current_user = request.user
    profile = profileUser.objects.get(user=current_user)

    if request.method == 'POST':
        form = NeighborHoodForm(request.POST)

        if form.is_valid():
            hood = form.save(commit=False)
            hood.resider = current_user
            hood.save()
            print(hood)

            return redirect('profile', current_user.id)
        
    else:
        form = NeighborHoodForm()

    return render(request, 'neighbor.html', {'form' : form})

@login_required
def posts(request):
    posts = Posts.objects.all()

    return render(request, 'posts.html', {'posts': posts})

@login_required
def create_post(request):
    current_user = request.user

    profile = profileUser.objects.get(user=current_user)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = current_user
            post.save()

        return redirect('posts',)

    else:
        form = PostForm()

    return render(request, 'new_posts.html', {'form' : form})