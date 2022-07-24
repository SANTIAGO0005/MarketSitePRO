# Generated by Django 4.0.6 on 2022-07-23 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sales', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='invoicedetails',
            options={'verbose_name': 'Detalle de Factura', 'verbose_name_plural': 'Detalles de Factura'},
        ),
        migrations.AlterModelOptions(
            name='tax',
            options={'verbose_name': 'Impuesto', 'verbose_name_plural': 'Impustos'},
        ),
        migrations.RemoveField(
            model_name='invoicedetails',
            name='PencetagePrice',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='percentage',
        ),
        migrations.AddField(
            model_name='invoicedetails',
            name='PrecentagePrice',
            field=models.IntegerField(default=0, verbose_name='Precio Porcentual'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tax',
            name='precentage',
            field=models.IntegerField(default='0', verbose_name='Porcentaje'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='CreateAt',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Invoice_CreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='DeleteBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Invoice_DeleteBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='DeletedAt',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='InvoiceDate',
            field=models.DateField(verbose_name='Fecha de Factura'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='InvoiceNumber',
            field=models.CharField(max_length=50, verbose_name='Numero de Factura'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ModifiedAt',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Modificacion'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ModifiyBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Invoice_ModifiyBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='CodeP',
            field=models.CharField(max_length=50, verbose_name='codigo del producto'),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='CostP',
            field=models.IntegerField(verbose_name='Costo del Producto'),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='Desc',
            field=models.CharField(max_length=50, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='Precentage',
            field=models.IntegerField(verbose_name='Porcentaje'),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='PriceP',
            field=models.IntegerField(verbose_name='Precio del Producto'),
        ),
        migrations.AlterField(
            model_name='invoicedetails',
            name='Quality',
            field=models.IntegerField(verbose_name='Calidad'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='desc',
            field=models.CharField(max_length=50, verbose_name='Descripcion'),
        ),
    ]
