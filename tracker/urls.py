from django.urls import path

from tracker.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic_delete"),
]

app_name = "tracker"
