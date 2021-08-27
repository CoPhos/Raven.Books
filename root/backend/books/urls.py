from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('BookDetail/<uuid:pk>/', BookDetail.as_view()),
    path('bookList/', BookList.as_view()),
]