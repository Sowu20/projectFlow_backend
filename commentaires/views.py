from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Commentaire
from .serializers import RegisterCommentaireSerializer, UpdateCommentaireSerializer, ListeCommentaireSerializer, CommentaireDetailSerializer
from drf_yasg.utils import swagger_auto_schema

class RegisterCommentaireView(generics.CreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = RegisterCommentaireSerializer

    @swagger_auto_schema(
        operation_description="Ajouter un commentaire.",
        responses={
            201: "Commentaire avec succès !",
            400: "Données invalides !"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UpdateCommentaireView(generics.UpdateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = UpdateCommentaireSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="Modifier un commentaire.",
        responses={
            201: "Commentaire modifiée avec succès !",
            400: "Données invalides !"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class ListCommentaireView(generics.ListAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = ListeCommentaireSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            201: "Liste des commentaires !",
            400: "Donnés invalides !"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class DeleteCommentaireView(APIView):
    def delete(self, id):
        try:
            commentaire = Commentaire.objects.get(id=id)
            commentaire.delete()
            return Response(
                {
                    "Commentaire supprimée avec succès !"
                }, status=204
            )
        except Commentaire.DoesNotExist:
            return Response(
                {
                    "Commentaire introuvable !"
                }, status= 400
            )

class CommentaireDetailView(RetrieveAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireDetailSerializer
    lookup_field = 'id'