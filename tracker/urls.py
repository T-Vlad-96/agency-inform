from django.urls import path

from tracker.views import (
    index,
    TopicListView,
    TopicCreateView
)

urlpatterns = [
    path("", index, name="index"),

    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topic_create/", TopicCreateView.as_view(), name="topic_create"),
]

app_name = "tracker"
