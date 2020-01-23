from django import forms
from conversion.models import SaveConverter


class ConverterForm(forms.Form):
    class Meta:
        model = SaveConverter
        field =('result_converter')


