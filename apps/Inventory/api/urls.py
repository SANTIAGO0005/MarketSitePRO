from django.urls import path
from apps.Sales.views import InvoiceListAPIWiew

urlpatterns = [
    path('Inventory/',InvoiceListAPIWiew.as_view(),name='Inventario'),
]
