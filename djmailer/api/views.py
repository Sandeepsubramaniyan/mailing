from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import SubscriberSerializer
from .models import Subscriber


class SubscriberView(APIView):
    
    def get(self,request):
        return Response({"message": "hello world!"})
    
    def post(self,request):
        serializer=SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber_instance = Subscriber.objects.create(**serializer.data)
        
            return Response({"message":"Created Subscriber{}".format(subscriber_instance.id)})
        else:
            return Response({"errors":serializer.errors})
     


