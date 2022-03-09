from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import Response
from .serializers import SubscriberSerializer
from .models import Subscriber


class SubscriberView(ListAPIView,CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
     


