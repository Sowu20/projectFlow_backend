from django.contrib import admin
from .models import Projet

class ProjetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titre',
        'description',
        'statut',
        'manager',
        'equipe',
        'date_debut',
        'date_echeance',
        'date_echeance',
        'nombre_projet',
        'projet_termines',
        'projet_encours',
        'taux_avancement'
    )

admin.site.register(Projet, ProjetAdmin)