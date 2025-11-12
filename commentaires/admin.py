from django.contrib import admin
from .models import Commentaire

class CommentaireAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'contenu',
        'tache',
        'date_creation'
    )

admin.site.register(Commentaire, CommentaireAdmin)