from rest_framework import serializers

from to_do_list.board.models import Board
from to_do_list.status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(
        queryset=Board.objects,
    )

    class Meta:
        model = Status
        fields = [
            'id',
            'name',
            'order',
            'board'
        ]
