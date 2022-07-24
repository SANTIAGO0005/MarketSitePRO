from rest_framework.routers import DefaultRouter
from apps.Sales.views import InvoiceWiewSet, InvoiceDetailWiewSet

router = DefaultRouter()

router.register('Invoice', InvoiceWiewSet)
router.register('InvoiceDetails', InvoiceDetailWiewSet)

urlpatterns = router.urls