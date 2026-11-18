from rest_framework.viewsets import ModelViewSet

from .serializers import VeiculoSerializer
from .models import Veiculo


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer