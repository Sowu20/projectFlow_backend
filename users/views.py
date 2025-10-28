from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from .models import User
from .serializers import UserDetailSerializer, UserSerializer, LoginSerializer, RegisterUserSerializer, UpdateUserSerializer, DetailUserSerializer, UserListByRoleSerializer, ManagerSerializer, ListeManagerSerializer
from .permissions import IsAdmin
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserDetailByIdView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            user_data = UserSerializer(user).data

            return Response({
                'user': user_data,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    @swagger_auto_schema(
        operation_description="Créer un nouveau compte utilisateur.",
        responses={201: "Utilisateur créé avec succès", 400: "Données invalides"}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Modifier un nouveau compte utilisateur.",
        responses={201: "Utilisateur modifié avec succès", 400: "Données non modifié"}
    )
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class GetUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DetailUserSerializer

    @swagger_auto_schema(
        responses={201: "Liste des utilisateurs", 400: "Données invalides"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class DeleteUserView(APIView):
    def delete(self, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({
                "Utilisateur supprimé avec succès !"
            }, status=204)
        except User.DoesNotExist:
            return Response({
                "Utilisateur introuvable !"
            }, status=400)

class UsersByRoleView(generics.ListAPIView):
    serializer_class = UserListByRoleSerializer

    def get_queryset(self):
        role = self.request.query_params.get('role')
        valid_roles = ['client', 'collaborateur', 'manager', 'admin']
        if role in valid_roles:
            return User.objects.filter(role__iexact=role)
        return User.objects.filter(role__in=valid_roles)
    
class ManageDetailView(RetrieveAPIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id, role='manager')
        serializer = ManagerSerializer(user)

        return Response(serializer.data)
    
class ManagerListView(generics.ListAPIView):
    serializer_class = ListeManagerSerializer

    def get_queryset(self):
        return User.objects.filter(role='manager')

class AdminOnlyView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": "Bienvenue Admin !"}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = f""
            
            send_mail(
                "Réinitialisation de mot de passe",
                f"Cliquez sur ce lien pour réinitialiser votre mot de passe : {reset_link}",
                # settings.DEFAULT_FROM_EMAIL,
                # [email],
                # fail_silently=False,
            )
            return Response({
                "message": "Lien de réinitialisation de mot de passe envoyé"
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "error": "Aucun utilisateur trouvé !"
            }, status=status.HTTP_404_NOT_FOUND)
        
class ResetPassworConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({
                "error": "Lien invalide"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not default_token_generator.check_token(user, token):
            return Response({
                "error": "Token invalide ou expiré !"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        new_password = request.data.get("password")
        if not new_password:
            return Response({
                "error": "Le mot de passe est requis !"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        return Response({
            "message": "Mot de passe réinitialisé avec succès !"
        }, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    def put(self, request):
        user = request.user
        new_password = request.data.get("new_password")

        if not new_password:
            return Response({
                "error": "Le nouveau mot de passe est requis !"
            }, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({
            "message": "Mot de passe modifié avec succès !"
        }, status=status.HTTP_200_OK)