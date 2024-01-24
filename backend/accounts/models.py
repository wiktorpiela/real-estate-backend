from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to = 'profile_pictures/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) -> str:
        return f'Profile of {self.seller.username}'
