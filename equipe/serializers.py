from rest_framework import serializers
from .models import Equipe
from users.models import User

class EquipeSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    manager_username = serializers.CharField(source='manager.username', read_only=True)

    class Meta:
        model = Equipe
        fields = [
            'id',
            'membres',
            'manager',
            'manager_username',
            'date_creation'
        ]

class RegisterEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = [
            'membres',
            'manager',
            'date_creation'
        ]

class UpdateEquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = [
            'membres',
            'manager'
        ]

class ListeEquipeSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField()

    class Meta:
        model = Equipe
        fields = [
            'id',
            'membres',
            'manager',
            'date_creation'
        ]

class DetailEquipeSerializer(serializers.ModelSerializer):
    manager = serializers.CharField(source="user.username")

    class Meta:
        model = Equipe
        fields = [
            'id',
            'membres',
            'manager',
            'date_creation'
        ]