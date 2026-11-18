from rest_framework.test import APITestCase
from rest_framework import status

from .models import Cliente


class ClientesTestCase(APITestCase):

    def test_cadastar_cliente(self):
        url = "/clientes/"

        dados = {
            "nome": "João da Silva",
            "cpf": "12345678901",
            "email": "joao@example.com"
        }

        response = self.client.post(url, dados, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)