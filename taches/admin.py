from django.contrib import admin
from .models import Tache

class TacheAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',
        'statut',
        'collaborateur',
        'projet',
        'date_echeance'
    )

admin.site.register(Tache, TacheAdmin)