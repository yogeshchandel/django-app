from rest_framework.response import Response
from rest_framework import status
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.
class BookCreateView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        """List all books"""
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new book"""
        print("request.data:", request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """Retrieve a book by id"""
        book = self.get_object(pk)
        if not book:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """Update a book by id"""
        book = self.get_object(pk)
        if not book:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a book by id"""
        book = self.get_object(pk)
        if not book:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    