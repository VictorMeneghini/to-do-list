from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from to_do_list.board.models import Board
from .serializers import BoardSerializer
# from to_do_list.api.v1.pagination import PostLimitOffsetPagination


class BoardViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
