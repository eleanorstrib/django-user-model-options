from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=6)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['zip_code', 'password']

    def __str__(self):
        return self.email
