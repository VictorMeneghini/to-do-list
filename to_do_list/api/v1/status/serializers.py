from rest_framework import serializers

from to_do_list.status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'name',
            'order'
        ]
