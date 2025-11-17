from rest_framework import serializers
from .models import Projet
from users.models import User
from equipe.models import Equipe

class ProjetSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    manager_username = serializers.CharField(source='manager.username', read_only=True)
    equipe = serializers.PrimaryKeyRelatedField(queryset=Equipe.objects.all(), required=False)
    equipe_nom = serializers.CharField(source='equipe.nom', read_only=True)

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'manager',
            'equipe',
            'date_debut',
            'date_echeance',
            'manager_username',
            'equipe_nom'
        ]

class RegisterProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'manager',
            'equipe'
        ]

class UpdateProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = [
            'titre',
            'description',
            'manager',
            'equipe'
        ]

class ListProjetSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField()
    equipe = serializers.StringRelatedField()

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'date_debut',
            'date_echeance',
            'manager',
            'equipe'
        ]

class ProjetDetailSerilizer(serializers.ModelSerializer):
    manager = serializers.CharField(source='user.username')
    equipe = serializers.CharField(source='equipe.nom')

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'description',
            'date_debut',
            'date_echeance',
            'manager',
            'equipe'
        ]

class ProjetStatsSerializer(serializers.ModelSerializer):
    nombre_projet = serializers.SerializerMethodField()
    projet_termines = serializers.SerializerMethodField()
    projet_encours = serializers.SerializerMethodField()
    taux_avancement = serializers.SerializerMethodField()

    class Meta:
        model = Projet
        fields = [
            'id',
            'titre',
            'nombre_projet',
            'projet_termines',
            'projet_encours',
            'taux_avancement'
        ]

    def get_nombre_projet(self, obj):
        return Projet.objects.filter(projet=obj).count()
    
    def get_projet_termines(self, obj):
        return Projet.objects.filter(projet=obj, statut='termine').count()
    
    def get_projet_encours(self, obj):
        return Projet.objects.filter(projet=obj, statut='en_cours').count()
    
    def get_taux_avancement(self, obj):
        total = self.get_nombre_projet(obj)
        termines = self.get_projet_termines(obj)
        return round((termines/total * 100, 2) if total > 0 else 0)