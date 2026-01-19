from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User

class postView(generics.ListCreateAPIView):
    queryset=postModel.objects.all()
    serializer_class=postSerializer
    permission_classes=[AllowAny]

class updatePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset=postModel.objects.all()
    serializer_class=postSerializer
    permission_classes=[IsAuthenticated]

class userPostsView(generics.ListAPIView):
    serializer_class=postSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        # request_name=self.kwargs["name"]
        # request_user = get_object_or_404(User,username=request_name)
        # return postModel.objects.filter(user_id=request_user.id)
        user=self.request.user
        return postModel.objects.filter(user=user)