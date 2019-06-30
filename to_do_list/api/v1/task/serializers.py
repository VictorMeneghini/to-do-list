from rest_framework import serializers

from to_do_list.status.models import Status
from to_do_list.task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects,
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'description',
            'status'
        ]
