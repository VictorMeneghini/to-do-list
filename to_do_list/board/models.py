from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):

    name = models.CharField(
        max_length=50,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
