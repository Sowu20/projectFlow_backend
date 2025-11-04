from rest_framework import serializers
from .models import Projet
from users.models import User

class ProjetSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    manager_username = serializers.CharField(source='manager.username', read_only=True)

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'manager',
            'date_debut',
            'date_echeance',
            'manager_username'
        ]

class RegisterProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'descriptions',
            'manager'
        ]

class UpdateProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'titre',
            'description',
            'manager'
        ]

class ListProjetSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField()

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'date_debut',
            'date_echeance',
            'manager'
        ]