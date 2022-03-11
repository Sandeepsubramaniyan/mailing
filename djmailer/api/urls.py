from rest_framework.routers import SimpleRouter
from .views import SubscriberViewSet
from .views import login
from django.conf.urls import url


router = SimpleRouter()
router.register("subscribers",SubscriberViewSet)



urlpatterns = router.urls + [
    
    url(r'^login', login)
]