from rest_framework import generics
from .models import Book, BookImage
from .serializers import BookSerializer, BookImageSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookImageList(generics.ListAPIView):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer