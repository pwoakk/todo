from django import forms

from .models import Comment, Task
from ..accounts.models import User, ManagerProfile, WorkerProfile
from ..job.models import Department


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class TaskCreateForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=ManagerProfile.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}),)
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}),)
    performer = forms.ModelChoiceField(queryset=WorkerProfile.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}),)

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'description',
            'deadline',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


