from rest_framework.test import APITestCase
from rest_framework import status

from clientes.models import Cliente
from veiculos.models import Veiculo
from .models import Permanencia


class PermanenciasTestCase(APITestCase):
    
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="João da Silva",
            cpf="12345678901",
            email="joao@example.com"
        )
        self.veiculo = Veiculo.objects.create(
            proprietario=self.cliente,
            marca="Toyota",
            modelo="Corolla",
            ano=2020,
            placa="ABC1234"
        )

    def test_registrar_entrada(self):
        url = "/permanencias/registrar-entrada/"

        dados = {
            "veiculo": self.veiculo.id,
            "vaga": "A1"
        }

        response = self.client.post(url, dados, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Permanencia.objects.count(), 1)

    def test_registrar_saida(self):
        permanencia = Permanencia.objects.create(
            veiculo=self.veiculo,
            vaga="A1"
        )

        url = f"/permanencias/{permanencia.id}/registrar-saida/"

        response = self.client.put(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Permanencia.objects.get(id=permanencia.id).saida)
        self.assertIsNotNone(Permanencia.objects.get(id=permanencia.id).tempo_permanencia)
        self.assertIsNotNone(Permanencia.objects.get(id=permanencia.id).valor)