from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('client', 'Client'),
        ('collaborateur', 'Collaborateur'),
        ('manager', 'Manager'),
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=65)
    image = models.ImageField(upload_to="users/", blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    date_inscription = models.DateField(auto_now_add=True)