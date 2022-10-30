from django.db import models
from apps.User.models import Bussines, User
from apps.Base.models import BaseModel, DetailsBaseModel
 
# Create your models here.

class Pushcase(BaseModel):
    """Model definition for Pushcase."""
    
    PushcaseNumeber = models.CharField(max_length=50,unique=True,null=False,blank=False)
    EnterpriceId = models.ForeignKey(Bussines, on_delete=models.CASCADE,null=True)
    PushcaseDate = models.DateField(auto_now=False, auto_now_add=True,null=True)
    CreatedBy = models.ForeignKey(User,related_name='Pushcase_CreatedBy',on_delete=models.CASCADE, null=True)
    ModifiyBy = models.ForeignKey(User,related_name='Pushcase_ModifiyBy',on_delete=models.CASCADE, null=True)
    DeleteBy =  models.ForeignKey(User,related_name='Pushcase_DeleteBy',on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f'{self.PushcaseNumeber}'


class PushcaseDetail(DetailsBaseModel):
    """Model definition for PushcaseDetail."""

    PushcaseId = models.ForeignKey(Pushcase, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Dedatalle de compra"
        verbose_name_plural = "Detalles de compras"

    def __str__(self):
       return f'{self.Desc} {self.CodeProduct} {self.CostProduct} {self.quantity}'
