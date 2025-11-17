from django.contrib import admin
from .models import Tache

class TacheAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titre',
        'description',
        'statut',
        'collaborateur',
        'projet'
    )

admin.site.register(Tache, TacheAdmin)