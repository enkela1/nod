from django.db import models
from django.contrib.auth.models import AbstractUser


ONBOARDING_PROGRESS = [
    ("0", "sign up"), 
    ("1", "detail"), 
    ("2", "about"),
    ("3", "quick questions")
]

class Tag(models.Model): 
    name = models.CharField(max_length=40, unique=True)
    type = models.CharField(max_length=20)


class User(AbstractUser): 
    name = models.TextField(max_length=80)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="users")
    onboarding_progress = models.CharField(
        max_length=30, 
        choices=ONBOARDING_PROGRESS, 
        default="0"
    )
