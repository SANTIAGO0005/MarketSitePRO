from django.contrib import admin
from apps.Sales.models import *
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceDetails)
admin.site.register(Tax)