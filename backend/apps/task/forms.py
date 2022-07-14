from django import forms

from .models import Comment, Task
from ..accounts.models import User, ManagerProfile, WorkerProfile
from ..job.models import Department


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class TaskCreateForm(forms.ModelForm):
    performer = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                               widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Исполнитель'}))

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            'author',
            'department',
            'performer',
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Отдел'}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'description',
            'deadline',
            'performer',
            'status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'performer': forms.CheckboxSelectMultiple(),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


