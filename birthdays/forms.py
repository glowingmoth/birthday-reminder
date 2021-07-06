from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Birthday


class BirthdayForm(ModelForm):
    class Meta:
        model = Birthday
        exclude = ('created_by',)
        widgets = { 'birthDate': TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),}  # Read docs = widgets

       