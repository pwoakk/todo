from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from backend.apps.task.models import *


class IndexPage(ListView):
    template_name = "index.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task" # стандартный object
    extra_context = {'comments': Comment.objects.all()}
