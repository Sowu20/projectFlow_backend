from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import models
from django.db.models import Q
from users.models import User
from .models import Projet
from .serializers import ProjetSerializer, RegisterProjetSerializer, UpdateProjetSerializer, ListProjetSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegisterProjetView(generics.CreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = RegisterProjetSerializer

    @swagger_auto_schema(
        operation_description="Créer une nouveau projet.",
        responses={
            201: "Projet créé avec succès !", 
            400: "Données invalides !"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateProjetView(generics.UpdateAPIView):
    queryset = Projet.objects.all()
    serializer_class = UpdateProjetSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Modifier un projet.",
        responses={
            201: "Projet modifié avec succès !",
            400: "Données invalides !"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class ListeProjetView(generics.ListAPIView):
    queryset = Projet.objects.all()
    serializer_class = ListProjetSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            201: "Liste des catégories !",
            400: "Données invalides !"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class DeleteProjetView(APIView):
    def delete(self, id):
        try:
            projet = Projet.objects.get(id=id)
            projet.delete()
            return Response(
                {"Projet supprimé avec succès !"}, status=204
            )
        except Projet.DoesNotExist:
            return Response(
                {"Projet introuvable !"}, status=400
            )