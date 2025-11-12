from django.urls import path
from .views import RegisterEquipeView, UpdateEquipeView, ListEquipeView, DeleteEquipeView, EquipeDetailView

urlpatterns = [
    path('register_team/', RegisterEquipeView.as_view(), name='register_team'),
    path('update_team/<int:id>/', UpdateEquipeView.as_view(), name='update_team'),
    path('list_team/', ListEquipeView.as_view(), name='list_team'),
    path('delete_team/<int:id>/', DeleteEquipeView.as_view(), name='delete_team'),
    path('detail_team/<int:id>/', EquipeDetailView.as_view(), name='detail_team'),
]