from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    name = models.CharField(blank=True, max_length=255)


    def __str__(self):
        return self.email
