from django.db import models
from apps.User.models import User
from apps.Product.models import Product
# Create your models here.
#
class Inventory(models.Model):

    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    state = models.BooleanField(default=True,null=True)
    quantity = models.IntegerField(null=True)
    CreatedBy = models.ForeignKey(User,related_name='Inventory_CreatedBy',on_delete=models.CASCADE,null=True)
    ModifiyBy = models.ForeignKey(User,related_name='Inventory_ModifiyBy',on_delete=models.CASCADE,null=True)
    DeleteBy =  models.ForeignKey(User,related_name='Inventory_DeleteBy',on_delete=models.CASCADE,null=True)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return f'{self.ProductId} {self.state} {self.quantity}'