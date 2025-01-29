from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker.models import (
    Topic,
    Redactor,
    Newspaper,
)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = ("id", ) + UserAdmin.list_display + ("years_of_experience", )
    search_fields = ("username",)
    ordering = ("id",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "years_of_experience",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Experience", {"fields": ("years_of_experience",)}),
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "get_topics",
        "get_publishers",
        "published_date"
    )

    search_fields = ("title",)
    list_filter = ("topics",)
    ordering = ("id",)

    def get_topics(self, obj):
        return ", ".join([topic.name for topic in obj.topics.all()])

    def get_publishers(self, obj):
        return ", ".join(
            [
                f"{publisher.first_name} {publisher.last_name}"
                for publisher in obj.publishers.all()
            ]
        )
