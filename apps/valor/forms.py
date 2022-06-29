from dataclasses import field
from django import forms
from .models import ValorModel


class ValorForm(forms.ModelForm):
    class Meta:
        model = ValorModel
        fields = [
            'valor',
            'sensor'
        ]