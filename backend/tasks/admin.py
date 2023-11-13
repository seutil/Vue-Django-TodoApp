from django.contrib import admin

from . import models as tasks_models


@admin.register(tasks_models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'status']
    list_display_links = ['title']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['status']
    search_fields = ['title']
    date_hierarchy = 'created'
