from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'image',
            'role',
            'date_inscription'
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('Ce compte est inactif !')
                data['user'] = user
            else:
                raise serializers.ValidationError("Nom d'utilisateur ou mot de passe incorrect !")
        else:
            raise serializers.ValidationError("les champs sont obligatoire !")

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'password',
            'role'
        )

    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            nom = validate_data['nom'],
            prenom = validate_data['prenom'],
            email = validate_data['email'],
            password = validate_data['password'],
            role = validate_data['role']
        )
        return user
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'role'
        )
        extra_kwargs = {
            'email': {'required': False},
            'username': {'required': False},
            'role': {'required': False},
        }

class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'password',
            'image',
            'role',
            'date_inscription'
        )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'password',
            'image',
            'role',
            'date_inscription'
        )

class UserListByRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'role',
            'date_inscription'
        )

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'image',
            'role',
            'date_inscription'
        )

class ListeManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nom',
            'prenom',
            'email',
            'image',
            'role',
            'date_inscription'
        )