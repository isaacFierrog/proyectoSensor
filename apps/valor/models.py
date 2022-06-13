from django.db import models
from apps.sensor.models import SensorModel


class ValorModel(models.Model):
    valor_id = models.AutoField(primary_key=True)
    valor = models.PositiveIntegerField(default=0)
    sensor = models.ForeignKey(SensorModel, on_delete=models.CASCADE)
