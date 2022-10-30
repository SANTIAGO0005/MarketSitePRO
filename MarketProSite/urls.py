
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.User.views import login, Logout

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v1',
      description="Documentacion publica de API MarketSitePro",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cifuentess938@mail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('users',include('apps.User.api.routers')),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(),name='logout'),
    path('login/',login.as_view(),name='login'),
    path('products/',include('apps.Product.api.routers')),
    path('pushcases/',include('apps.PushCase.api.routers')),
    path('Sales/',include('apps.Sales.api.routers')),
    path('Inventorys/',include('apps.Inventory.api.routers')),

]

