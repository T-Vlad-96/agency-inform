from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    TopicSearchForm,
    RedactorSearchForm,
    NewspaperSearchForm,
    RedactorCreateForm,
)

from tracker.models import Topic, Redactor, Newspaper


@login_required
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

class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    paginate_by = 5
    search_form = TopicSearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search_form = TopicSearchForm(self.request.GET)
        if search_form.is_valid():
            return self.queryset.filter(
                name__icontains=search_form.cleaned_data["name"]
            )
        return self.queryset


class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("tracker:topic_list")


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("tracker:topic_list")


class TopicDeleteView(LoginRequiredMixin, DeleteView):
    model = Topic
    template_name = "tracker/topic_delete_confirm.html"
    success_url = reverse_lazy("tracker:topic_list")


# *** The Redactor model views ***

class RedactorListView(LoginRequiredMixin, ListView):
    model = Redactor
    paginate_by = 5
    search_form = RedactorSearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        self.queryset = super().get_queryset()
        search_form = RedactorSearchForm(self.request.GET)
        if search_form.is_valid():
            return self.queryset.filter(
                username__icontains=search_form.cleaned_data["username"]
            )
        return self.queryset


class RedactorDetailView(LoginRequiredMixin, DetailView):
    model = Redactor


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    )
    success_url = reverse_lazy("tracker:redactor_list")


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("tracker:redactor_list")


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    template_name = "tracker/redactor_delete_confirm.html"
    success_url = reverse_lazy("tracker:redactor_list")


# *** The Newspaper model views ***


class NewspaperListView(LoginRequiredMixin, ListView):
    model = Newspaper
    paginate_by = 5
    search_form = NewspaperSearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        self.queryset = super().get_queryset().prefetch_related(
            "topics", "publishers"
        )
        search_form = NewspaperSearchForm(self.request.GET)
        if search_form.is_valid():
            return self.queryset.filter(
                title__icontains=search_form.cleaned_data["title"]
            )
        return self.queryset


class NewspaperDetailView(LoginRequiredMixin, DetailView):
    model = Newspaper


class NewspaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("tracker:newspaper_list")


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("tracker:newspaper_list")


class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    template_name = "tracker/newspaper_delete_confirm.html"
    success_url = reverse_lazy("tracker:newspaper_list")
