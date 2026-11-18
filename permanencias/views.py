from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

from .models import Permanencia
from .serializers import PermanenciaSerializer
from .serializers import RegistrarSaidaSerializer


class PermanenciaViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin, 
    viewsets.GenericViewSet
):
    queryset = Permanencia.objects.all()
    serializer_class = PermanenciaSerializer

    @action(detail=False, methods=['post'], url_path='registrar-entrada')
    def registrar_entrada(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        permanencia = serializer.save()

        return Response(
            self.get_serializer(permanencia).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['put'], url_path='registrar-saida', 
    serializer_class=RegistrarSaidaSerializer)
    def registrar_saida(self, request, pk=None):
        permanencia = self.get_object()

        if permanencia.saida is not None:
            return Response(
                {"detail": "Saída já registrada para esta permanência."},
                status=status.HTTP_400_BAD_REQUEST
            )

        permanencia.saida = timezone.now()
        permanencia.tempo_permanencia = (
            permanencia.saida - permanencia.entrada
        )
        permanencia.valor = self.calcular_valor(permanencia.tempo_permanencia)
        permanencia.save()

        return Response(
            self.get_serializer(permanencia).data,
            status=status.HTTP_200_OK
        )

    def calcular_valor(self, tempo_permanencia):
        taxa_por_hora = 5.00  
        horas = tempo_permanencia.total_seconds() / 3600
        return round(horas * taxa_por_hora, 2)