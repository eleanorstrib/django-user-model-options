from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=6)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username
