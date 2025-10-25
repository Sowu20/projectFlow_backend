from django.db import models
from django.conf import settings

class Projet(models.Model):
    titre = models.CharField(max_length=40)
    description = models.TextField(null=True)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='manager', on_delete=models.CASCADE)