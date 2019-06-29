from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


from to_do_list.api.v1.board.views import BoardViewSet
from to_do_list.api.v1.status.views import StatusViewSet
from to_do_list.api.v1.task.views import TaskViewSet

router = routers.SimpleRouter()
router.register('boards', BoardViewSet)
router.register('status', StatusViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
