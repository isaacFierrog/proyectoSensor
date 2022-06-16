from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ValorSerializer
from apps.sensor.models import SensorModel


class ValorViewSet(viewsets.ModelViewSet):
    serializer_class = ValorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.all()

        return self.serializer_class.Meta.model.objects.filter(valor_id=pk).first()
    
    def retrieve(self, request, pk):
        valores_sensor = SensorModel.objects.filter(sensor_id=pk).first()
        valores_filtrados = list(valores_sensor.valormodel_set.all().values('valor').values_list('valor', flat=True))
        
        return Response({
            'mensaje': 'Hola',
            'data': valores_filtrados
        }, status=status.HTTP_200_OK)
