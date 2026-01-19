
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/login/',TokenObtainPairView.as_view(),name="gettokens"),
    path('api/refresh/',TokenRefreshView.as_view(),name="refresh"),
    path("api/",include('authentication.urls')),
    path("posts/",include("products.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)