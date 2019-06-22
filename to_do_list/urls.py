from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', include('to_do_list.board.urls', namespace='board')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
