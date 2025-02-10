from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)   
    email = models.EmailField(default="vul@gmail.com")  
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username