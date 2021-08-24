from django.urls import path
from .views import BookList, BookDetail, BookImageList

urlpatterns = [
    path('<int:pk>/', BookDetail.as_view()),
    path('', BookImageList.as_view())
]