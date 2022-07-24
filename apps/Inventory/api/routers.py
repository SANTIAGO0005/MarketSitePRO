from rest_framework.routers import DefaultRouter
from apps.Inventory.views import InventoryViewset

router = DefaultRouter()
router.register('Inventory', InventoryViewset)

urlpatterns = router.urls