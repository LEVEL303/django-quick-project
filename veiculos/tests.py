from rest_framework.test import APITestCase
from rest_framework import status


from clientes.models import Cliente
from .models import Veiculo


class VeiculosTestCase(APITestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="João da Silva",
            cpf="12345678901",
            email="joao@example.com"
        )

    def test_cadastrar_veiculo(self):
        url = "/veiculos/"

        dados = {
            "proprietario": self.cliente.id,
            "marca": "Toyota",
            "modelo": "Corolla",
            "ano": 2020,
            "placa": "ABC1234"
        }

        response = self.client.post(url, dados, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Veiculo.objects.count(), 1)
    
