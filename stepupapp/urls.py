from rest_framework.routers import DefaultRouter
from .views import NumberViewSet

router = DefaultRouter()
router.register('numbers', NumberViewSet)

urlpatterns = router.get_urls()
