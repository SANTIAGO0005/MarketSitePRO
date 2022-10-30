from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    CreateAt = models.DateField(auto_now=False, auto_now_add=True)
    ModifiedAt = models.DateField(auto_now=True, auto_now_add=False)
    DeletedAt = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Modelo Base"
        verbose_name_plural = "Modelos Base"

class DetailsBaseModel(models.Model):

    CodeProduct = models.CharField(max_length=50,unique=True,null=True,blank=False,default=False)
    Desc =  models.CharField(max_length=50, null=True)
    quantity =  models.IntegerField(null=True,default=False)
    PriceProduct = models.IntegerField(null=True,default=False)
    CostProduct = models.IntegerField(null=True,default=False)
    UnitProduct =  models.CharField(max_length=50,null=True,default=False)
    Precentage = models.CharField(max_length=10,null=True)
    PrecentagePrice = models.IntegerField(null=True)
    Total = models.IntegerField(null=True)

    class Meta:
        abstract = True
        verbose_name = "Detalle Base de moedelos"
        verbose_name_plural = "Detalles Base de moedelos"