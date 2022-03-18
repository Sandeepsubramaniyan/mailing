from rest_framework.viewsets import ModelViewSet
from .serializers import SubscriberSerializer , RegisterSerializer
from .models import Subscriber
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (IsAuthenticated,)
    

@api_view(["POST"])  
def login(request):
    username=request.data.get("username")
    password = request.data.get("password")
    
    user = authenticate(username=username,password=password)
    
    if not user:
        return Response({"error": "Login failed"},status = HTTP_401_UNAUTHORIZED)
    
    (token,created)= Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


    
@api_view(["POST"])  
def register(request):
    serializer= RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user= serializer.save() 
    
    (token)= Token.objects.create(user=user)
    return Response({
        'user_info': {
            'username':user.username,
            'email':user.email,
            },
        "token": token.key
        })
    
    
    
    

            
            
            
        





