from rest_framework import serializers

from to_do_list.board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Board
        fields = [
            'id',
            'name',
            'status',
            'description'
        ]

    def create(self, validate_data):
        instance = super().create(validate_data)
        instance.owner.add(self.context.get('request').user)
        instance.save()
        return instance
