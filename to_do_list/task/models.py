from django.db import models
from to_do_list.status.models import Status


class Task(models.Model):

    class Meta:
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')

    name = models.CharField(
        max_length=20,
        blank=False
    )

    description = models.TextField(
        null=False,
        max_length=255,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='tasks')

    def __str__(self):
        return self.name
