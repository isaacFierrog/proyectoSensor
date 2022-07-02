from django.shortcuts import render, redirect
from .models import SensorModel


def listar_sensor(request):
    sensores = SensorModel.objects.filter(estado=True)
    return render(request, 'sensor/listar_sensor.html', {
        'sensores': sensores
    })


def crear_sensor(request):
    if request.method == 'POST':
        if 'crear_sensor' in request.POST:
            sensor_id:str = hex(SensorModel.objects.count() + 1).split('0x')[1]
            SensorModel.objects.create(
                sensor_id=sensor_id
            )
            return redirect('sensor:listar_sensor')
    
    return render(request, 'sensor/crear_sensor.html')


def eliminar_sensor(request, id):
    print(id)
    sensor = SensorModel.objects.filter(sensor_id=id, estado=True).first()
    print(sensor)
    
    if request.method == 'POST':
        sensor.estado = False
        sensor.save()
        return redirect('sensor:listar_sensor')
        
    return render(request, 'sensor/eliminar_sensor.html', {
        'sensor': sensor
    })