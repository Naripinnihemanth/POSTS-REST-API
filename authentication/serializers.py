from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","first_name","last_name","email"]
        extra_kwargs={  
            "password":{
                "write_only":True
            }
        }


    
