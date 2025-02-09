from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            #UserProfile.objects.create(user=user)
            
            UserProfile.objects.create(user=user,  email=user.email)
            
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})


def home(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})


def user_logout(request):
    logout(request)
    return redirect('home')

#------------


def search_view_form(request):
    query_username = request.GET.get("username", "")  # Get "username" from URL
    query_email = request.GET.get("email", "")  # Get "email" from URL
    query_blood_group = request.GET.get("blood_group", "")

    # Apply filtering based on user and email
    results = UserProfile.objects.filter(
        user__username__icontains=query_username,  # Search for matching username
        email__icontains=query_email, # Search for matching email
        blood_group__icontains=query_blood_group
    )

    return render(request, "search_result.html", {"results": results})
