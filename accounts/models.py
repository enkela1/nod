from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Tag(models.Model): 
    name = models.CharField(max_length=40, unique=True)
    type = models.CharField(max_length=20)


class User(AbstractUser): 
    name = models.TextField(max_length=80)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="users")
    onboarding_done = models.BooleanField(default=False)