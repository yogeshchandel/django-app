from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializer import AuthorSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class AuthorListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer