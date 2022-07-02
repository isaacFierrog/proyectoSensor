from django.urls import path
from .views import listar_sensor, crear_sensor, eliminar_sensor


urlpatterns = [
    path('listar/', listar_sensor, name='listar_sensor'),
    path('crear/', crear_sensor, name='crear_sensor'),
    path('eliminar/<id>/', eliminar_sensor, name='eliminar_sensor')
]