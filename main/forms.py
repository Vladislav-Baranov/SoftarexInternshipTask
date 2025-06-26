from django import forms
from .models import Calculations


class CalculationsForm(forms.ModelForm):
    class Meta:
        model = Calculations
        fields = ['img']
