from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager
class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username = None
    is_deleted=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=CustomUserManager()

    def __str__(self):
        return self.email
    def soft_del(self):
        self.is_deleted=True
        self.save()