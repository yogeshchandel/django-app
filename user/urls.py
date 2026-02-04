
from .views import RegisterView, LoginView, UserViewSet
from django.urls import path, include
from rest_framework import routers

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', UserViewSet.as_view({'get': 'list'}), name='user-list'),
]