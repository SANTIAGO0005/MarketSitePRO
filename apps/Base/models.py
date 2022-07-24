from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    IsDeleted = models.BooleanField(default=True)
    CreateAt = models.DateField('Fecha de Creacion',auto_now=False, auto_now_add=True)
    ModifiedAt = models.DateField('Fecha de Modificacion',auto_now=True, auto_now_add=False)
    DeletedAt = models.DateField('Fecha de Eliminacion',auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Modelo Base"
        verbose_name_plural = "Modelos Base"

class DetailsBaseModel(models.Model):

    CodeP = models.CharField(verbose_name='codigo del producto',max_length=50)
    Desc =  models.CharField(verbose_name='Descripcion',max_length=50)
    Quality =  models.IntegerField(verbose_name='Calidad')
    PriceP = models.IntegerField(verbose_name='Precio del Producto')
    CostP = models.IntegerField(verbose_name='Costo del Producto')
    UnitP =  models.CharField(max_length=50)
    Precentage = models.IntegerField(verbose_name='Porcentaje')
    PrecentagePrice = models.IntegerField(verbose_name='Precio Porcentual')
    Total = models.IntegerField()

    class Meta:
        abstract = True
        verbose_name = "Detalle Base de moedelos"
        verbose_name_plural = "Detalles Base de moedelos"