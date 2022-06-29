from django.shortcuts import render
from .forms import SensorForm


def sensores(request):
    return render(request, 'sensor/sensor.html')