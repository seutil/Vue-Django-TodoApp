from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views as tasks_views


router = DefaultRouter()
router.register('tasks', tasks_views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
