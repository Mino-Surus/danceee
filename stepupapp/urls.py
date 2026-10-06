from rest_framework.routers import DefaultRouter
from .views import DancebandViewSet, DancerViewSet

router = DefaultRouter()
router.register('danceband', DancebandViewSet)
router.register('dancer', DancerViewSet)


urlpatterns = router.get_urls()
