from django.urls import path
from .views import RegisterCommentaireView, UpdateCommentaireView, ListCommentaireView, DeleteCommentaireView, CommentaireDetailView

urlpatterns = [
    path('register_comment/', RegisterCommentaireView.as_view(), name='register_comment'),
    path('update_comment/<int:id>/', UpdateCommentaireView.as_view(), name='update_comment'),
    path('list_comment/', ListCommentaireView.as_view(), name='list_comment'),
    path('delete_comment/<int:id>/', DeleteCommentaireView.as_view(), name='delete_comment'),
    path('detail_comment/<int:id>/', CommentaireDetailView.as_view(), name='detail_comment'),
]