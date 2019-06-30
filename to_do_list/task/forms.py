from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label='Task Name',
        required=True,
        max_length=255,
    )

    description = forms.CharField(
        label='Task Description',
        required=True,
        max_length=255,
    )

    def __init__(self, status=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if status:
            self.instance.status = status

    class Meta:
        fields = [
            'name',
            'description'
        ]
        model = Task
