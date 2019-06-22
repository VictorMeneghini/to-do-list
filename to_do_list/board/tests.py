from django.test import TestCase

from to_do_list.authentication.models import User

from .models import Board


class BoardTestCase(TestCase):

    def setUp(self):
        owner = User.objects.create_user('fake@user.com', 'user', 12345678)
        Board.objects.create('teste', 'teste', owner)
        return owner
