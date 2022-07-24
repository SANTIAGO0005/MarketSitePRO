from apps.Sales.models import Tax, Invoice, InvoiceDetails
from rest_framework import serializers
from apps.Product.api.serializers import ProductSerializer
from apps.User.api.serializers import BusinessSerializer
from apps.User.api.serializers import UserListSerializer

class TaxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tax
        fields = '__all__'
        

class InvoiceSerializer(serializers.ModelSerializer):
    
    EnterpriceId = serializers.StringRelatedField()
    TaxId = serializers.StringRelatedField()
    # CreatedBy = serializers.StringRelatedField()
    # ModifiyBy = serializers.StringRelatedField()
    # DeleteBy = serializers.StringRelatedField()
    
    class Meta:
        model = Invoice
        exclude = ('IsDeleted','CreateAt','ModifiedAt','DeletedAt','Taxid','CreatedBy','ModifiyBy','DeleteBy','AmoutMin','AmountMax',)

class InvoiceDetailsSerializer(serializers.ModelSerializer):
    InvoiceId = serializers.StringRelatedField()
    ProductId = serializers.StringRelatedField()
    class Meta:
        model = InvoiceDetails
        fields = '__all__'