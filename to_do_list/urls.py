from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('to_do_list.board.urls', namespace='board')),
    path('status/', include('to_do_list.status.urls', namespace='status')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
