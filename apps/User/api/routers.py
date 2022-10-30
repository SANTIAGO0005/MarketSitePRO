from rest_framework.routers import DefaultRouter

from apps.User.api.api import UserViewSet, BusinessWiewSet

router = DefaultRouter()

router.register('User', UserViewSet, basename="user")
router.register('Business', BusinessWiewSet)

urlpatterns = router.urls