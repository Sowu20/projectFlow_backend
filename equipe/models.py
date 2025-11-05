from django.db import models
from django.conf import settings

class Equipe(models.Model):
    nom = models.CharField(max_length=40)
    date_creation = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsable', on_delete=models.CASCADE)
    membres = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='equipe', blank=True)