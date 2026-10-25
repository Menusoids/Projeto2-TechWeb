from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rawg_id']