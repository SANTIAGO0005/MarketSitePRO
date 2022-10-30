from django.db import models
import apps.User.models
import apps.Sales.models
from apps.Base.models import BaseModel


# Create your models here.
class CategoryProduct(models.Model):
    """Model definition for CategoryProduct."""

    NameCategory = models.CharField('Nombre de categoria', max_length=50,unique=True, null = False, blank= False)

    class Meta:
            verbose_name = 'Categoria'
            verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.NameCategory}'

class Product(BaseModel):
    """Model definition for Product."""
    
    CodeProduct = models.CharField(max_length=50,unique=True,null=False,blank=False)
    NameProduct = models.CharField(max_length=50,null=True,default=False)
    CategoryId = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,null=True)
    AmoutMin = models.IntegerField(null=True)
    AmountMax = models.IntegerField(null=True)
    PriceProduct = models.IntegerField(null=True,default=False)
    CostProduct = models.IntegerField(null=True,default=False)
    Taxid = models.ForeignKey(apps.Sales.models.Tax, on_delete=models.CASCADE,null=True)
    CreatedBy = models.ForeignKey(apps.User.models.User,related_name='Product_CreatedBy',on_delete=models.CASCADE,null=True)
    ModifiyBy = models.ForeignKey(apps.User.models.User,related_name='Product_ModifiyBy',on_delete=models.CASCADE,null=True)
    DeleteBy =  models.ForeignKey(apps.User.models.User,related_name='Product_DeleteBy',on_delete=models.CASCADE,null=True)
    

    class Meta:
            verbose_name = 'producto'
            verbose_name_plural = 'productos'

    def __str__(self):
        return f'{self.NameProduct}'