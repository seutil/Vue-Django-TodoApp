from rest_framework import serializers as rest_serializers

from . import models as tasks_models


class TaskSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = tasks_models.Task
        fields = ['id', 'owner', 'title', 'status', 'description']
