from django.shortcuts import render

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
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['not_started_tasks'] = Task.objects.filter(status=Task.STATUS_NOT_STARTED)
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
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        task = Task.objects.filter(id=self.kwargs['pk'])
        pk = self.kwargs["pk"]

        context['task'] = task
        context['comments'] = Comment.objects.filter(task=pk)
        context['form'] = form

        if form.is_valid():
            name = request.user
            text = form.cleaned_data['text']

            comment = Comment.objects.create(
                name=name, text=text, task=task
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


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

