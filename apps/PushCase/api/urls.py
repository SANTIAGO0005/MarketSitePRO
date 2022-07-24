from django.urls import path
from apps.PushCase.views import PushcaseListAPIWiew, PushcaseDetailsListAPIWiew

urlpatterns = [
    path('pushcase/',PushcaseListAPIWiew.as_view(),name='compra'),
    path('pushcase/',PushcaseDetailsListAPIWiew.as_view(),name='Detalle_de_compra'),
]
