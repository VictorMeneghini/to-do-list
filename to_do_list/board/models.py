from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):

    class Meta:
        verbose_name = ("Board")
        verbose_name_plural = ("Boards")

    name = models.CharField(
        max_length=50,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    owner = models.ManyToManyField(User)

    def __str__(self):
        return self.name
