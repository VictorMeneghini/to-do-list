from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from to_do_list.task.models import Task
from .serializers import TaskSerializer


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
