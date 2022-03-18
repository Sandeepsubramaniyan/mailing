from django.contrib.auth.models import User
from rest_framework import serializers , validators
from .models import  Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Subscriber
        fields = '__all__'
        
        
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {
            'password' :{'write_only': True},
            'email':{
                'required':True,
                'allow_blank':False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(),"A user with that email already exists"
                        
                    )
                ]
                
            }
        }
        
    
    def create(self,validated_data):
        
        return User.objects.create_user(**validated_data)


            

        