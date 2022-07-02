from django.db import models


class SensorModel(models.Model):
    sensor_id = models.CharField(
        max_length=4, 
        primary_key=True, 
        blank=True
    )
    estado = models.BooleanField(
        'Estado del sensor',
        default=True
    )
    fecha_creacion = models.DateField(
        'Fecha de creacion',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        verbose_name = "sensor"
        verbose_name_plural = "sensores"
        db_table = "sensor"

    def __str__(self):
        return f"<Sensor: {self.sensor_id}>"
