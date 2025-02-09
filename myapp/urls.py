from django.urls import path
from .views import register, user_login, profile, home,user_logout,search_view_form

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
    path('search_koro/', search_view_form, name='search_view_form'),
     path('logout/', user_logout, name='logout'),
]