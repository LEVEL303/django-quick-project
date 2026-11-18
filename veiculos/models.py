from django.db import models

from clientes.models import Cliente


class Veiculo(models.Model):
    proprietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    placa = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.placa}"