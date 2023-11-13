from rest_framework import (viewsets as rest_viewsets,
                            authentication as rest_authentication,
                            permissions as rest_permissions)

from . import models as tasks_models
from . import serializers as tasks_serializers


class TaskViewSet(rest_viewsets.ModelViewSet):
    queryset = tasks_models.Task.objects.all()
    serializer_class = tasks_serializers.TaskSerializer
    permission_classes = [rest_permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [rest_authentication.BasicAuthentication]
