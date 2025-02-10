from django.urls import path
from .views import register, user_login, profile, home,user_logout,search,contact,about

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
     path('logout/', user_logout, name='logout'),
]