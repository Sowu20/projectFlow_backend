from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Equipe
from users.models import User
from .serializers import RegisterEquipeSerializer, UpdateEquipeSerializer, ListeEquipeSerializer, DetailEquipeSerializer
from drf_yasg.utils import swagger_auto_schema

class RegisterEquipeView(generics.CreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = RegisterEquipeSerializer

    @swagger_auto_schema(
        operation_description="Créer une équipe.",
        responses={
            201: "Equipe créé avec succès !",
            400: "Données invalides !"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateEquipeView(generics.UpdateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = UpdateEquipeSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Modifier une équipe.",
        responses={
            201: "Equipe modifiée avec succès !",
            400: "Données invalides !"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class ListEquipeView(generics.ListAPIView):
    queryset = Equipe.objects.all()
    serializer_class = ListeEquipeSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            201: "Liste des équipes !",
            400: "Donnés invalides !"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class DeleteEquipeView(APIView):
    def delete(self, id):
        try:
            equipe = Equipe.objects.get(id=id)
            equipe.delete()
            return Response(
                {
                    "Equipe supprimée avec succès !"
                }, status=204
            )
        except Equipe.DoesNotExist:
            return Response(
                {
                    "Equipe introuvable !"
                }, status= 400
            )

class EquipeDetailView(RetrieveAPIView):
    queryset = Equipe.objects.all()
    serializer_class = DetailEquipeSerializer
    lookup_field = 'id'