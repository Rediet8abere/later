from django.urls import path
from .views import (
    BooksListView,
    BooksDetailView,
    BooksCreateView
)

from . import views

urlpatterns = [
    path('', BooksListView.as_view(), name='book-home'),
    path('<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('new/', BooksCreateView.as_view(), name='book-create'),
]
