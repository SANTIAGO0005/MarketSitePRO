from django.urls import path
from apps.Sales.views import TaxListAPIWiew, InvoiceListAPIWiew, InvoiceDetailsListAPIWiew

urlpatterns = [
    path('Tax/',TaxListAPIWiew.as_view(),name='Impuesto'),
    path('Invoice/',InvoiceListAPIWiew.as_view(),name='venta'),
    path('InvoiceDetails/',InvoiceDetailsListAPIWiew.as_view(),name='Detalle_de_venta'),
]
