from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CreateTask, UpdateTask, TaskDelete

app_name = 'tasks'
urlpatterns = [
    path('create/<int:pk>', login_required(CreateTask.as_view()), name='task_create'),
    path('update/<int:pk>', login_required(UpdateTask.as_view()), name='task_update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task_delete')
]
