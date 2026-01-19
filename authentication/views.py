from django.shortcuts import render
from rest_framework import generics
from .serializers  import *
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import *

class usersView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer
    permission_classes=[AllowAny]

class singleUser(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer
    permission_classes=[AllowAny]
# class userDataView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset=User.objects.all()
#     serializer_class=userSerializer
#     permission_classes=[AllowAny]
#     lookup_field="id"

