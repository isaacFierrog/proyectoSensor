from django.db import models
from apps.sensor.models import SensorModel


class ValorModel(models.Model):
    valor_id = models.AutoField(primary_key=True)
    valor = models.PositiveIntegerField(default=0)
    sensor = models.ForeignKey(SensorModel, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'valor'
        verbose_name_plural = 'valores'
        db_table = 'valor'
        
    def __str__(self):
        return f'<Valor: {self.valor}>'
