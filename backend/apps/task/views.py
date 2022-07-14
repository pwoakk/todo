from django import shortcuts
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from backend.apps.task.models import *
from .forms import CommentForm, TaskCreateForm, TaskUpdateForm


class IndexPage(ListView):
    template_name = "index.html"
    model = Task

    def get_context_data(self, **kwargs):
        update_form = TaskUpdateForm
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['not_started_tasks'] = Task.objects.filter(status=Task.STATUS_NOT_STARTED)
        context['task_update_form'] = update_form
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    object = "task"

    def get_context_data(self, **kwargs):
        print(kwargs['object'].id)
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        form = CommentForm()
        context['comments'] = Comment.objects.filter(task=pk)
        # context['comments'] = Comment.objects.filter(task=kwargs['object'].id)

        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]

        task = Task.objects.get(id=pk)
        comments = Comment.objects.filter(task=task)

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.task = task
                instance.save()
            return redirect('task_detail', pk=task.id)
        else:
            form = CommentForm()
        context = {
            'task': task,
            "form": form,
            'comments': comments
        }

        return render(request, 'task_detail.html', context)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('index')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('index')


class TaskUpdateModalView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('index')


def task_delete(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        task.delete()
    else:
        pass
    return redirect('index')


class ProjectListView(ListView):
    template_name = "project_list.html"
    model = Project
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['range'] = range(1,5)
        return context

