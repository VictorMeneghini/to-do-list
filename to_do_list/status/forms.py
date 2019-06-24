from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        label="Column Name",
        required=True,
        max_length=255,
    )

    order = forms.IntegerField()

    def save(self, board_id):
        instance = super().save(commit=False)
        instance.board_id = board_id
        instance.save()
        return instance

    class Meta:
        fields = [
            "name",
            "order"
        ]
        model = Status
