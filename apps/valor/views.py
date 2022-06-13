from rest_framework import viewsets
from .serializers import ValorSerializer


class ValorViewSet(viewsets.ModelViewSet):
    serializer_class = ValorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.all()

        return self.serializer_class.Meta.model.objects.filter(id=pk).first()
