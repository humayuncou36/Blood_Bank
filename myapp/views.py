from django.core.paginator import Paginator
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

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST,request.FILES, instance=request.user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserProfileForm(instance=request.user.userprofile)
#     return render(request, 'profile.html', {'form': form})


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same or another view
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form, 'profile': profile})



def home(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})


def user_logout(request):
    logout(request)
    return redirect('home')

#------------



def search(request):
    query_username = request.GET.get('username', '')
    query_email = request.GET.get('email', '')
    query_blood_group = request.GET.get('blood_group', '')

    results = UserProfile.objects.all()
    
    results = UserProfile.objects.filter(
        user__username__icontains=query_username,
        email__icontains=query_email,
        blood_group__icontains=query_blood_group
   )

    # Paginate results (9 users per page)
    paginator = Paginator(results, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_result.html', {'page_obj': page_obj})



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')
