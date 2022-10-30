from apps.PushCase.models import Pushcase, PushcaseDetail
from rest_framework import serializers
from apps.Product.api.serializers import ProductSerializer
from apps.User.api.serializers import BusinessSerializer
from apps.User.api.serializers import UserListSerializer

class PushcaseSerializer(serializers.ModelSerializer):
    EnterpriceId = serializers.StringRelatedField()
    # CreatedBy = serializers.StringRelatedField()
    # ModifiyBy = serializers.StringRelatedField()
    # DeleteBy = serializers.StringRelatedField()
    
    class Meta:
        model = Pushcase
        exclude = ('state','CreateAt','ModifiedAt','DeletedAt','CreatedBy','ModifiyBy','DeleteBy')

class PushcaseDetailSerializer(serializers.ModelSerializer):
    ProductId = serializers.StringRelatedField()
    PushcaseId = serializers.StringRelatedField()
    
    class Meta:
        model = PushcaseDetail
        fields = '__all__'