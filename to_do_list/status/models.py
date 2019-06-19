from django.db import models
from to_do_list.board.models import Board

class Status(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False
    )

    order = models.IntegerField()

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='status')

    def __str__(self):
        return self.name