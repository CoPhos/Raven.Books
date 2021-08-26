from rest_framework import generics
from .models import Book, BookImage, Authors, Tags, Publisher
from .serializers import BookSerializer, BookDetailSerializer, BookImageSerializer, PublisherSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class BookList(generics.ListAPIView):
    """
        GET all books with its fields
    """    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['publication_year',]
    pagination_class = PageNumberPagination

class BookDetail(generics.RetrieveAPIView):
    """
        GET one book with its fields
        the book id must be in the path
    """  
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer