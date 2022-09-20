from django.contrib import admin

from django101.tasks.models import task


@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    pass
