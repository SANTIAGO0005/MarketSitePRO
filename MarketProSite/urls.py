
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('apps.User.api.routers')),
    path('admin/', admin.site.urls),
    path('products/',include('apps.Product.api.routers')),
    path('pushcases/',include('apps.PushCase.api.routers')),
    path('Sales/',include('apps.Sales.api.routers')),
    path('Inventorys/',include('apps.Inventory.api.routers')),

]

