from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.all()

        return self.serializer_class.Meta.model.objects.filter(sensor_id=pk).first()

    def retrieve(self, request, *args, **kwargs):
        valores_sensor = list(self.get_object().valormodel_set.all().values("valor"))

        if not valores_sensor:
            return Response(
                {"Error": "No se encontraron valores asociado al sensor"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        valores = [valor["valor"] for valor in valores_sensor]

        return Response(
            {"mensaje": "Listado de valores", "data": {"valores": valores}},
            status=status.HTTP_200_OK,
        )
