from django.contrib import admin
from django.urls import path, include

from backend.apps.accounts.views import (
    LoginView,
    UserRegisterView,
    RegisterDoneView,
    user_logout,
    UserUpdateView, UserPasswordChangeView, ManagerProfileView, DirectorProfileView
    # update_user_profile
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout/', user_logout, name='logout'),
    path('user/change-password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/profile/<int:pk>/', ManagerProfileView.as_view(), name='profile'),
    path('user/dprofile/', DirectorProfileView.as_view(), name='profile'),
    path('user/profile1/', DirectorProfileView.as_view(), name='profile'),
]