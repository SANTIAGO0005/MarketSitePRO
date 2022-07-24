from rest_framework.routers import DefaultRouter
from apps.PushCase.views import PushcaseWiewSet, PushcaseDetailsWiewSet

router = DefaultRouter()
router.register('Pushcase', PushcaseWiewSet)
router.register('PushcaseDetails', PushcaseDetailsWiewSet)

urlpatterns = router.urls