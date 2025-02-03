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