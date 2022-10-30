from rest_framework import viewsets
from apps.Inventory.api.serializers import InventorySerializer

# Create your views here.
class InventoryViewset(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = InventorySerializer.Meta.model.objects.filter(state=True)

    