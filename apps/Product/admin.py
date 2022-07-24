from django.contrib import admin
from apps.Product.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(CategoryProduct)