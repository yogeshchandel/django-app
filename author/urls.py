from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView
from rest_framework import routers

app_name = 'author'
urlpatterns = [
    path('authors', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
]