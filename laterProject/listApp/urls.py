from django.urls import path
from .views import (
    BooksListView,
    BooksDetailView,
    BooksCreateView,
    BooksUpdateView,
    BooksDeleteView
)

from . import views

urlpatterns = [
    path('', BooksListView.as_view(), name='book-home'),
    path('<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('new/', BooksCreateView.as_view(), name='book-create'),
    path('<int:pk>/update', BooksUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete', BooksDeleteView.as_view(), name='book-delete'),
]
