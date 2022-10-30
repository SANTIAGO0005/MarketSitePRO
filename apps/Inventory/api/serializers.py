from apps.Inventory.models import Inventory
from rest_framework import serializers
from apps.Product.api.serializers import ProductSerializer
from apps.User.api.serializers import UserListSerializer

class InventorySerializer(serializers.ModelSerializer):
    ProductId = serializers.StringRelatedField()
    # CreatedBy = serializers.StringRelatedField()
    # ModifiyBy = serializers.StringRelatedField()
    # DeleteBy = serializers.StringRelatedField()
    
    class Meta:
        model = Inventory
        exclude = ('CreatedBy','ModifiyBy','DeleteBy')

