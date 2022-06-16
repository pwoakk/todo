from django import forms

from .models import Comment, Task


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"})
        }


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "deadline": forms.DateTimeInput(attrs={"class": "form-control"}),
        }
