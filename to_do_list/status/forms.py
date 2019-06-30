from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        label="Column Name",
        required=True,
        max_length=255,
    )

    order = forms.IntegerField()

    def __init__(self, board=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if board:
            self.instance.board = board

    class Meta:
        fields = [
            "name",
            "order"
        ]
        model = Status
