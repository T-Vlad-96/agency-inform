from django.urls import path

from tracker.models import Redactor, Newspaper
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
    RedactorDeleteView,

    NewspaperListView,

)

urlpatterns = [
    path("", index, name="index"),

    # Topic routes:
    path("topics/", TopicListView.as_view(), name="topic_list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/update/<int:pk>/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic_delete"),

    # Redactor routes:
    path("redactors/", RedactorListView.as_view(), name="redactor_list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor_detail"),
    path("redactor/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactor_update"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor_create"),
    path("redactor/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactor_delete"),

    # Newspaper routes:
    path("newspapers/", NewspaperListView.as_view(), name="newspaper_list"),
]

app_name = "tracker"
