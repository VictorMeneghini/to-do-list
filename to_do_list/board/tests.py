from django.test import TestCase

from .models import Board

class BoardTestCase(TestCase):

    def setUp(self):
        Board.objects.create(
            name="todo",
            description="this is a to do list",
            owner=1
        )
        