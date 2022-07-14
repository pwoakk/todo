from django.urls import path, include

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('detail/task/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', task_delete, name='task_delete'),
    path('task/update/', TaskUpdateView.as_view(), name='task_update'),
    path('project/list', ProjectListView.as_view(), name='project_list'),
    path('task/update/modal/<int:pk>/', TaskUpdateModalView.as_view(), name='task_modal'),
]
