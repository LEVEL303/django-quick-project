from django.db import models

from veiculos.models import Veiculo


class Permanencia(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    vaga = models.CharField(max_length=10)
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(null=True, blank=True)
    tempo_permanencia = models.DurationField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)