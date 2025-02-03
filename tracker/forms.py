from django import forms


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
