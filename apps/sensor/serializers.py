from dataclasses import fields
from rest_framework import serializers
from .models import SensorModel


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorModel
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        numero_de_sensores = SensorModel.objects.all().count()
        sensor_id = hex(numero_de_sensores + 1).split("0x")[1]

        return SensorModel.objects.create(sensor_id=sensor_id)
