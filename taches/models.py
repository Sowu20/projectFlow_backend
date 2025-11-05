from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
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
    collaborateur = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='collaborateur', on_delete=models.CASCADE, limit_choices_to={'role': 'collaborateur'})
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='projet')

    def clean(self):
        if self.collaborateur and self.projet.equipe and self.collaborateur not in self.projet.equipe.membres.all():
            raise ValidationError("Le collaborateur doit être membre de l'équipe du projet !")