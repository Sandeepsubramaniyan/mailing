from rest_framework.views import APIView
from rest_framework.views import Response
from .serializers import SubscriberSerializer
from .models import Subscriber


class HelloWorldView(APIView):
    
    def get(self,request):
        return Response({"message": "hello world!"})
    
    def post(self,request):
        serializer=SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            
            name = valid_data.get("name")
            age = valid_data.get("age")
        
            return Response({"message":"Hello {}! you are {} years old".format(name,age)})
        else:
            return Response({"errors":serializer.errors})
     


