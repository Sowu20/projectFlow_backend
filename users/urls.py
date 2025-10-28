from django.urls import path
from .views import UserDetailByIdView, LoginAPIView, RegisterUserView, UpdateUserView, GetUserView, DeleteUserView, UsersByRoleView, ManageDetailView, ManagerListView, AdminOnlyView, ResetPasswordView, ResetPassworConfirmView, ChangePasswordView

urlpatterns = [
    path('<int:id>/', UserDetailByIdView.as_view(), name='user_detail'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('update/<int:id>', UpdateUserView.as_view(), name='update_user'),
    path('list/', GetUserView.as_view(), name='list_user'),
    path('delete/<int:id>/', DeleteUserView.as_view(), name='delete_user'),
    path('role/', UsersByRoleView.as_view(), name='users_by_role'),
    path('manager/<int:id>', ManageDetailView.as_view(), name='manager_detail'),
    path('list_manager/', ManagerListView.as_view(), name='list_manager'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', ResetPassworConfirmView.as_view(), name='reset_password_confirm'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]