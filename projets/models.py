from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from equipe.models import Equipe

class Projet(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé')
    ]
    titre = models.CharField(max_length=40)
    description = models.TextField(null=True)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="en_cours")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='manager', on_delete=models.CASCADE, limit_choices_to={'role': 'manager'})
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        if self.date_echeance and self.date_debut and self.date_echeance <= self.date_debut:
            raise ValidationError("La date d'échéance dotre être après la date de début !")