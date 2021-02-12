from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewset import TaskViewSet

router=DefaultRouter()
router.register(r"task", TaskViewSet,basename='task')

urlpatterns = [
    path("",include(router.urls),name='task'),
]
