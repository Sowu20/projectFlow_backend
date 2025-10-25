from django.db import models
from django.conf import settings
from projets.models import Projet

class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée')
    ]
    titre = models.CharField(max_length=40)
    description = models.TextField(null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_echeance = models.DateTimeField(auto_now_add=True)
    collaborateur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='collaborateur', on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)