from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import logout


@login_required
def about(request):

    return render(request, 'about.html')

@login_required
def home(request):
    business = Bussiness.objects.all().order_by('-id')
    neighborhoods = NeighborHood.objects.all().order_by('-id')

    context = {'business': business, 'neighborhoods': neighborhoods}

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
def single_business(request, biz_id):
    biz = Bussiness.objects.filter(pk = biz_id)

    return render(request, 'single_biz.html', {'biz': biz})

@login_required
def single_neighbor(request, neg_id):
    neighbor = profileUser.objects.filter(user=neg_id)

    return render(request,'single_neighbor.html', {'neighbor': neighbor})


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
        form = BussinessForm(request.POST, request.FILES)

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
        form = NeighborHoodForm(request.POST, request.FILES)

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
    posts = Posts.objects.all().order_by('-id')

    return render(request, 'posts.html', {'posts': posts})

@login_required
def create_post(request):
    current_user = request.user

    profile = profileUser.objects.get(user=current_user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = current_user
            post.save()

        return redirect('posts',)

    else:
        form = PostForm()

    return render(request, 'new_posts.html', {'form' : form})

@login_required
def create_health(request):
    current_user = request.user
    profile = profileUser.objects.get(user=current_user)

    if  request.method == 'POST':
        form = HealthForm(request.POST, request.FILES)

        if form.is_valid():
            health =  form.save(commit=False)
            health.resider = current_user
            health.save()

            return redirect('centers')

    else:
        form = HealthForm()

    return render(request, 'health.html', {'form': form})

@login_required
def centers(request):
    health = Health.objects.all().order_by('-id')

    return render(request, 'centers.html', {'health': health})

@login_required
def police(request):
    police = Police.objects.all().order_by('-id')

    return render(request, 'police.html', {'police': police})

@login_required
def create_police(request):
    current_user = request.user
    profile = profileUser.objects.get(user=current_user)

    if request.method == 'POST':
        form = PoliceForm(request.POST, request.FILES)

        if form.is_valid():
            police = form.save(commit=False)
            police.save()

            return redirect('police')

    else:
        form = PoliceForm()

    return render(request, 'create_police.html', {'form': form})