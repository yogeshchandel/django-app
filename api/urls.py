from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import Home

app_name = 'api'

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('user.urls')),
    path('', include('author.urls')),
    path('', include('book.urls')),
]
