from rest_framework.views import APIView
from rest_framework.views import Response


class HelloWorldView(APIView):
    
    def get(self,request):
        return Response({"message": "hello world!"})
     


