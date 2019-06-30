from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', include('to_do_list.board.urls', namespace='board')),
    path('status/', include('to_do_list.status.urls', namespace='status')),
    path('task/', include('to_do_list.task.urls', namespace='task')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('to_do_list.api.v1.urls')),
    path('docs/', include_docs_urls(title='To do List'))
]
