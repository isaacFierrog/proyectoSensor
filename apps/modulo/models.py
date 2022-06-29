from click import version_option
from django.db import models


class ModuloModel(models.Model):
    modulo_id = models.CharField(
        max_length=4,                          
        primary_key=True, 
        blank=True
    )
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'
        db_table = 'modulo'
        
    def __str__(self):
        return f"<Modulo: {self.modulo_id}>"
