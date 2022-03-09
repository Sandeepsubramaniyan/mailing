from django.conf.urls import url
from .views import SubscriberViewSet

urlpatterns = [
    url(r'^subscriber',SubscriberViewSet.as_view(),name="subscriber")
]
