from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('BookDetail/<int:pk>/', BookDetail.as_view()),
    path('bookList/', BookList.as_view()),
]