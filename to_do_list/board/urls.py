from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import Index, CreateBoard, BoardDelete, BoardUpdate

app_name = 'boards'
urlpatterns = [
    path('', login_required(Index.as_view()), name='index'),
    path('create/', login_required(CreateBoard.as_view()), name="board_create"),
    path('update/<int:pk>', login_required(BoardUpdate.as_view()), name="board_update"),
    path('delete/<int:pk>', BoardDelete.as_view(), name="board_delete"),
]