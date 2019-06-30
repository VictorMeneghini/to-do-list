from django.db import models
from to_do_list.board.models import Board


class Status(models.Model):

    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Status")

    name = models.CharField(
        max_length=20,
        blank=False
    )

    order = models.IntegerField()

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='status')

    def __str__(self):
        return self.name
