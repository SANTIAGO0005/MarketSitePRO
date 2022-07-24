from rest_framework.routers import DefaultRouter
from apps.Product.views import ProductViewSet, CategoryProductViewSet

router = DefaultRouter()

router.register('products',ProductViewSet)
router.register('CategoryProducts',CategoryProductViewSet)

urlpatterns = router.urls



