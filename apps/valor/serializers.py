from dataclasses import fields
from rest_framework import serializers
from .models import ValorModel


class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorModel
        fields = "__all__"
        read_only_fields = ["id"]
