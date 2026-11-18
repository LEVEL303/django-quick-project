from rest_framework import serializers
from .models import Permanencia

class PermanenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permanencia
        fields = '__all__'
        read_only_fields = ['entrada', 'saida', 'tempo_permanencia', 'valor']

class RegistrarSaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permanencia
        fields = []