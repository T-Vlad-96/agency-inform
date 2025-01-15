from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker.models import (
    Topic,
    Redactor,
    Newspaper,
)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
