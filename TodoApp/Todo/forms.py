from django import forms
from django.forms import ModelForm

from .models import DailyWorks


class DateInput(forms.DateInput):
    input_type = 'date'




class DailyWorksForm(ModelForm):
    class Meta:
        model = DailyWorks
        fields = ['goal', 'date', 'completed']
        widgets = {
            'date': DateInput(),
        }
