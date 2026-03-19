from rest_framework import serializers
from .models import Reserva
from clientes.serializers import ClienteSerializer
from estoque.serializers import PecaSerializer

class ReservaSerializer(serializers.ModelSerializer):
    cliente_detalhe = ClienteSerializer(source='cliente', read_only=True)
    peca_detalhe = PecaSerializer(source='peca', read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'