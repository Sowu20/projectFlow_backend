from django.db import models
from django.conf import settings
from taches.models import Tache

class Commentaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)