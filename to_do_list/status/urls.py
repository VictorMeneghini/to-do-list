from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CreateStatus, UpdateStatus, StatusDelete

app_name = 'status'
urlpatterns = [
    path('create/<int:pk>', login_required(CreateStatus.as_view()), name="status_create"),
    path('update/<int:pk>', login_required(UpdateStatus.as_view()), name="status_update"),
    path('delete/<int:pk>', StatusDelete.as_view(), name="status_delete")
]
