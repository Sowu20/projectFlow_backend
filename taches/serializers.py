from rest_framework import serializers
from .models import Tache
from users.models import User
from projets.models import Projet

class TacheSerializer(serializers.ModelSerializer):
    collaborateur = serializers.PrimaryKeyRelatedField(request=User.objects.all(), required=False) 
    projet = serializers.PrimaryKeyRelatedField(request=Projet.objects.all(), required=False)
    collaborteur_username = serializers.CharField(source='user.username', read_only=True)
    projet_nom = serializers.CharField(source='projet.nom', read_only=True)

    class Meta:
        model = Tache
        fields = [
            'id',
            'titre',
            'description',
            'statut',
            'collaborateur',
            'collaborateur_username',
            'projet',
            'projet_nom'
        ]

class RegisterTacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = {
            'titre',
            'description',
            'statut',
            'collaborateur',
            'projet'
        }

class UpdateTacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = [
            'titre',
            'description',
            'statut',
            'collaborateur',
            'projet'
        ]

class ListeTacheSerializer(serializers.ModelSerializer):
    collaborateur = serializers.StringRelatedField()
    projet = serializers.StringRelatedField()

    class Meta:
        model = Tache
        fields = [
            'id',
            'titre',
            'description',
            'statut',
            'collaborateur',
            'date_echeance',
            'projet'
        ]

class DetailTacheSerializer(serializers.ModelSerializer):
    collaborateur = serializers.CharField(source='user.username')
    projet = serializers.CharField(source='projet.nom')

    class Meta:
        model = User
        fields = [
            'id',
            'titre',
            'description',
            'statut',
            'collaborateur',
            'date_echeance',
            'projet'
        ]