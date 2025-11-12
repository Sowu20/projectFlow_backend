from django.contrib import admin
from .models import Equipe

class EquipeAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'manager',
        'membres',
        'date_creation'
    )

admin.site.register(Equipe, EquipeAdmin)