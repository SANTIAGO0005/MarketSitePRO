from rest_framework import viewsets
from apps.Sales.api.serializers import TaxSerializer, InvoiceSerializer, InvoiceDetailsSerializer

# Create your views here.
class TaxWiewSet(viewsets.ModelViewSet):
    serializer_class = TaxSerializer
    queryset = TaxSerializer.Meta.model.objects.all()

class InvoiceWiewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = InvoiceSerializer.Meta.model.objects.filter(state=True)

class InvoiceDetailWiewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceDetailsSerializer
    queryset = InvoiceDetailsSerializer.Meta.model.objects.all()

