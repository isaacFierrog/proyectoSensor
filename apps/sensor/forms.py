from django import forms
from .models import SensorModel


class SensorForm(forms.ModelForm):
    class Meta:
        model = SensorModel
        fields = [
            'sensor_id'
        ]