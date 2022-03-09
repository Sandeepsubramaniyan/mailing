from django.conf.urls import url
from .views import HelloWorldView, SubscriberView

urlpatterns = [
    url(r'^subscriber',SubscriberView.as_view(),name="subscriber")
]
