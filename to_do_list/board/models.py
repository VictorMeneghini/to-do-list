from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):

    class Meta:
        verbose_name = ("Board")
        verbose_name_plural = ("Boards")

    name = models.CharField(
        max_length=20,
        blank=False,
    )

    description = models.TextField(
        null=False,
        max_length=255,
        blank=False
    )

    owner = models.ManyToManyField(
        User,
        related_name='boards')

    def __str__(self):
        return self.name
