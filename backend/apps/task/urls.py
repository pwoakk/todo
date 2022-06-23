from django.urls import path, include

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('detail/task/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
]
