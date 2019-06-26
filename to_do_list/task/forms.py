from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label="Task Name",
        required=True,
        max_length=255,
    )

    description = forms.CharField(
        label="Task Description",
        required=True,
        max_length=255,
    )

    def save(self, status_id):
        instance = super().save(commit=False)
        instance.status_id = status_id
        instance.save()
        return instance

    class Meta:
        fields = [
            "name",
            "description"
        ]
        model = Task
