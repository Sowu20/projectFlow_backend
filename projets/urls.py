from django.urls import path
from .views import RegisterProjetView, UpdateProjetView, ListeProjetView, DeleteProjetView

urlpatterns = [
    path('register_project/', RegisterProjetView.as_view(), name='register_project'),
    path('update_project/<int:id>/', UpdateProjetView.as_view(), name='update_project'),
    path('list_project/', ListeProjetView.as_view(), name='list_project'),
    path('delete_project/<int:id>/', DeleteProjetView.as_view(), name='delete_project')
]
