from django.urls import path
from .views import *
urlpatterns=[
    path("register/",usersView.as_view(),name="register"),
    path("user/<int:pk>/",singleUser.as_view(),name="user"),
    # path("manipulate/<int:id>/",userDataView.as_view(),name="nanipulate"),
]