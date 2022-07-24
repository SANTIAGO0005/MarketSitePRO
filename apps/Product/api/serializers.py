from apps.Product.models import Product,CategoryProduct
from rest_framework import serializers
#from apps.Sales.api.serializers import TaxSerializer
#from apps.User.api.serializers import UserListSerializer

class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = '__all__'
   

class ProductSerializer(serializers.ModelSerializer):
    CategoryId = serializers.StringRelatedField()
    TaxId = serializers.StringRelatedField()
    # CreatedBy = serializers.StringRelatedField()
    # ModifiyBy = serializers.StringRelatedField()
    # DeleteBy = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('IsDeleted','CreateAt','ModifiedAt','DeletedAt','CreatedBy','ModifiyBy','DeleteBy','AmoutMin','AmountMax',) 
    
    
    '''si necesitaramos validar una imagen esta forma nos conviene mas'''
    # def to_representation(self, instance):
    #     return{
    #         'id':instance.id,
    #         'CodeP':instance.codeP,
    #         'NameP':instance.NameP,
    #         'CategoryId':instance.CategoryId.NameCategory,
    #         'Price':instance.Price,
    #         'Cost':instance.Cost
    #     }
    
               