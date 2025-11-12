from django.urls import path
from .views import RegisterTacheView, UpdateTacheView, ListTacheView, DeleteTacheView, TacheDetailView

urlpatterns = [
    path('register_task/', RegisterTacheView.as_view(), name='register_task'),
    path('update_task/<int:id>/', UpdateTacheView.as_view(), name='update_task'),
    path('list_task/', ListTacheView.as_view(), name='list_task'),
    path('delete_task/<int:id>/', DeleteTacheView.as_view(), name='delete_task'),
    path('detail_task/<int:id>/', TacheDetailView.as_view(), name='detail_task')    
]