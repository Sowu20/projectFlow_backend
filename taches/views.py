from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Tache
from users.models import User
from projets.models import Projet
from .serializers import RegisterTacheSerializer, UpdateTacheSerializer, ListeTacheSerializer, DetailTacheSerializer
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RegisterTacheView(generics.CreateAPIView):
    queryset = Tache.objects.all()
    serializer_class = RegisterTacheSerializer

    @swagger_auto_schema(
        operation_description="Créer une tâche.",
        responses={
            201: "Tâche créé avec succès !",
            400: "Données invalides !"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateTacheView(generics.UpdateAPIView):
    queryset = Tache.objects.all()
    serializer_class = UpdateTacheSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Modifier une tâche.",
        responses={
            201: "Tâche modifiée avec succès !",
            400: "Données invalides !"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class ListTacheView(generics.ListAPIView):
    queryset = Tache.objects.all()
    serializer_class = ListeTacheSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            201: "Liste des tâches !",
            400: "Donnés invalides !"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class DeleteTacheView(APIView):
    def delete(self, id):
        try:
            tache = Tache.objects.get(id=id)
            tache.delete()
            return Response(
                {
                    "Tâche supprimée avec succès !"
                }, status=204
            )
        except Tache.DoesNotExist:
            return Response(
                {
                    "Tâche introuvable !"
                }, status= 400
            )

class TacheDetailView(RetrieveAPIView):
    queryset = Tache.objects.all()
    serializer_class = DetailTacheSerializer
    lookup_field = 'id'