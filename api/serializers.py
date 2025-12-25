from rest_framework import serializers
from .models import Item, Categoria

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True, read_only=True)
    
    itens_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Item.objects.all(),
        source='itens'
    )
    
    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'itens', 'itens_ids']