from django.contrib import admin
from django.urls import path, include

from backend.apps.accounts.views import (
    LoginView,
    UserRegisterView,
    RegisterDoneView,
    user_logout,
    UserUpdateView,
    # update_user_profile
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout/', user_logout, name='logout'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]