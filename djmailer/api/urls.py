from rest_framework.routers import SimpleRouter
from .views import SubscriberViewSet

router = SimpleRouter()
router.register("Subscribers",SubscriberViewSet)

urlpatterns = router.urls