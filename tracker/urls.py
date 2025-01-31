from django.urls import path

from tracker.models import Redactor
from tracker.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorUpdateView,
    RedactorCreateView,

)

urlpatterns = [
    path("", index, name="index"),

    # Topic views:
    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic_delete"),

    # Redactor views:
    path("redactors/", RedactorListView.as_view(), name="redactor_list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor_detail"),
    path("redactor/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor_update"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor_create"),
]

app_name = "tracker"
