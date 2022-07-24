from django.db import models
from apps.User.models import User
from apps.Product.models import Product
# Create your models here.
#
class Inventory(models.Model):

    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    IsDeleted = models.BooleanField('Estado',default=True)
    Quality = models.IntegerField('Calidad')
    CreatedBy = models.ForeignKey(User,related_name='Inventory_CreatedBy',on_delete=models.CASCADE)
    ModifiyBy = models.ForeignKey(User,related_name='Inventory_ModifiyBy',on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,related_name='Inventory_DeleteBy',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return f'{self.ProductId}'