from django.urls import path

from tracker.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
)

urlpatterns = [
    path("", index, name="index"),

    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topic_create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic_update/<int:pk>/", TopicUpdateView.as_view(), name="topic_update"),
]

app_name = "tracker"
