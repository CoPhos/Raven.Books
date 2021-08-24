from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True) 
    email = models.CharField(max_length=320, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now,null=False, blank=False)
    profile_photo = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='customuser_ppoi'
    )
    customuser_ppoi = PPOIField()