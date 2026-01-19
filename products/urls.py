from django.urls import path
from .views import *
urlpatterns=[
    path("updatepost/<int:pk>/",updatePostView.as_view(),name="updatepost"),
    path("list/",postView.as_view(),name="listPosts"),
    path("userposts/",userPostsView.as_view(),name="userposts")
]