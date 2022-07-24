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
    
    CodeP = models.CharField('Codigo del producto',max_length=50,unique=True,null=False,blank=False)
    NameP = models.CharField('Nombre del producto',max_length=50)
    CategoryId = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,verbose_name='Categoria del Producto')
    AmoutMin = models.IntegerField('Cantidad Minima')
    AmountMax = models.IntegerField('Cantidad Maxima')
    Price = models.IntegerField('Precio')
    Cost = models.IntegerField('Costo')
    Taxid = models.ForeignKey(apps.Sales.models.Tax, on_delete=models.CASCADE,verbose_name='Impuesto')
    CreatedBy = models.ForeignKey(apps.User.models.User,related_name='Product_CreatedBy',on_delete=models.CASCADE)
    ModifiyBy = models.ForeignKey(apps.User.models.User,related_name='Product_ModifiyBy',on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(apps.User.models.User,related_name='Product_DeleteBy',on_delete=models.CASCADE)
    

    class Meta:
            verbose_name = 'producto'
            verbose_name_plural = 'productos'

    def __str__(self):
        return f'{self.NameP}'