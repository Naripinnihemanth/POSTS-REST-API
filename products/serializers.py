from rest_framework import serializers
from .models import *


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=postModel
        fields="__all__"
        extra_kwargs={
            "user":{
                "read_only":True
            }
        }