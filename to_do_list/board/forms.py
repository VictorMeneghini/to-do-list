from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    name = forms.CharField(
        label="Board Name",
        required=True,
        max_length=255,
    )

    description = forms.CharField(
        label="Description",
        required=True,
        max_length=255,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user

    class Meta:
        fields = [
            "name",
            "description"
        ]
        model = Board
