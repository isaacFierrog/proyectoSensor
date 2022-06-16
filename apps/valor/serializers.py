from rest_framework import serializers
from apps.sensor.serializers import SensorSerializer
from .models import ValorModel


class ValorSerializer(serializers.ModelSerializer):
    # sensor = SensorSerializer()
    class Meta:
        model = ValorModel
        fields = "__all__"
        read_only_fields = ["valor_id"]