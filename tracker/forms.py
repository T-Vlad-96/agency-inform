from django import forms
from django.contrib.auth.forms import UserCreationForm

from tracker.models import Redactor


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        label="",
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name",
            }
        ),

    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        label="",
        required=False,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
            }
        )
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by title"
            }
        )
    )


class RedactorCreateForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
