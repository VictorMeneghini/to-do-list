from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from to_do_list.status.models import Status
from .serializers import StatusSerializer


class StatusViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
