from django.db import models
import apps.User.models 
from apps.Base.models import BaseModel, DetailsBaseModel


# Create your models here.
class Tax(models.Model):
    """Model definition for Tax."""

    desc=  models.CharField('Descripcion', max_length=50)
    precentage = models.IntegerField('Porcentaje')

    class Meta:
        verbose_name = "Impuesto"
        verbose_name_plural = "Impustos"

    def __str__(self):
        return f'{self.desc} {self.precentage}'        

class Invoice(BaseModel):
    """Model definition for Invoice."""

    InvoiceNumber = models.CharField(max_length=50,null=True)
    EnterpriceId = models.ForeignKey(apps.User.models.Bussines, on_delete=models.CASCADE,null=True)
    TaxId =  models.ForeignKey(Tax, on_delete=models.CASCADE,null=True)
    InvoiceDate = models.DateField(auto_now=False, auto_now_add=True,null=True)
    CreatedBy = models.ForeignKey(apps.User.models.User,related_name='Invoice_CreatedBy',on_delete=models.CASCADE,null=True)
    ModifiyBy = models.ForeignKey(apps.User.models.User,related_name='Invoice_ModifiyBy',on_delete=models.CASCADE,null=True)
    DeleteBy =  models.ForeignKey(apps.User.models.User,related_name='Invoice_DeleteBy',on_delete=models.CASCADE,null=True)
   
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f'{self.InvoiceNumber}'



class InvoiceDetails(DetailsBaseModel):
    """Model definition for InvoiceDetails."""
    InvoiceId = models.ForeignKey(Invoice, on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"

    def __str__(self):
        return f'{self.Desc} {self.CodeProduct} {self.CostProduct} {self.quantity}'
