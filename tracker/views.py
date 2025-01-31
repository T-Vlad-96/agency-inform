from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from tracker.models import Topic, Redactor, Newspaper


def index(request: HttpRequest) -> HttpResponse:
    num_topics = Topic.objects.all().count()
    num_redactors = Redactor.objects.all().count()
    num_newspapers = Newspaper.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits
    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_visits": num_visits,
    }
    return render(request, "tracker/index.html", context=context)


# *** The Topic model views ***

class TopicListView(ListView):
    model = Topic
    paginate_by = 5


class TopicCreateView(CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("tracker:topic_list")


class TopicUpdateView(UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("tracker:topic_list")


class TopicDeleteView(DeleteView):
    model = Topic
    template_name = "tracker/topic_delete_confirm.html"
    success_url = reverse_lazy("tracker:topic_list")


# *** The Redactor model views ***

class RedactorListView(ListView):
    model = Redactor
    paginate_by = 5


class RedactorDetailView(DetailView):
    model = Redactor


class RedactorUpdateView(UpdateView):
    model = Redactor
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    )
    success_url = reverse_lazy("tracker:redactor_list")


class RedactorCreateView(CreateView):
    model = Redactor
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    )
    success_url = reverse_lazy("tracker:redactor_list")

