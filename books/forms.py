from django import forms
# import datetime as d


class QueryForm(forms.Form):
    date = forms.DateField(
        label='Date',
        required=True,
        widget=forms.DateInput(),
        input_formats=['%Y-%m-%d'],
    )
