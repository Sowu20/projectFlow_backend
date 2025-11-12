from django.contrib import admin
from .models import Projet

class ProjetAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',
        'statut',
        'manager',
        'equipe',
        'date_debut',
        'date_echeance'
    )

admin.site.register(Projet, ProjetAdmin)