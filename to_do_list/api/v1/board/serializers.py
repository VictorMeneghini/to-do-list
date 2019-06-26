from rest_framework import serializers

from to_do_list.board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'description'
        ]
