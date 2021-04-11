from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def home(request):

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request, prof_id):
    user = User.objects.get(pk = prof_id)
    title = User.objects.get(pk = prof_id).username
    profile = profileUser.objects.filter(user= prof_id)

    return render(request, 'profile.html', {"profile": profile})



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