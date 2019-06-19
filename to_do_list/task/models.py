from django.db import models
from to_do_list.status.models import Status

class Task(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='tasks')

    def __str__(self):
        return self.name
