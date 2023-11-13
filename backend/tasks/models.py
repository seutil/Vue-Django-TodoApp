from django.db import models
from django.contrib.auth import get_user_model


class TasksInProcessManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Task.Status.PROCESS)


class TasksDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Task.Status.DONE)


class Task(models.Model):
    class Status(models.TextChoices):
        PROCESS = 'P', 'Process'
        DONE = 'D', 'Done'

    owner = models.ForeignKey(get_user_model(), models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.PROCESS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    in_process = TasksInProcessManager()
    done = TasksDoneManager()
    objects = models.Manager()

    class Meta:
        db_table = 'tasks'
        ordering = ['created']

    def __str__(self):
        return self.title
