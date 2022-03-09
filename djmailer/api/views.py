from rest_framework.views import APIView
from rest_framework.views import Response


class HelloWorldView(APIView):
    
    def get(self,request):
        return Response({"message": "hello world!"})
    
    def post(self,request):
        name = request.data.get("name")
        if not name:
            return Response({"error":"No name passed"})
        return Response({"message":"Hello {}!".format(name)})
     


