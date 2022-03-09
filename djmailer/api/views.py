from rest_framework.generics import ListCreateAPIView
from .serializers import SubscriberSerializer
from .models import Subscriber


class SubscriberView(ListCreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
     


