from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

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


class TopicListView(ListView):
    model = Topic
    paginate_by = 5
