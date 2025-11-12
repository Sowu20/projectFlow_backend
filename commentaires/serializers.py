from rest_framework import serializers
from .models import Commentaire
from users.models import User

class CommentaireSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Commentaire
        fieds = [
            'id',
            'user',
            'user_username',
            'contenu',
            'tache',
            'date_creation'
        ]

class RegisterCommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = [
            'user',
            'contenu',
            'tache',
            'date_creation'
        ]

class UpdateCommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = [
            'user',
            'contenu',
            'tache'
        ]

class ListeCommentaireSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Commentaire
        fields = [
            'id',
            'user',
            'contenu',
            'tache',
            'date_creation'
        ]

class CommentaireDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Commentaire
        fields = [
            'id',
            'user',
            'contenu',
            'tache',
            'date_creation'
        ]