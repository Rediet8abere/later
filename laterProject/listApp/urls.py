from django.urls import path, include
from .views import (
    HomeView,
    BooksListView,
    BooksDetailView,
    BooksCreateView,
    BooksUpdateView,
    BooksDeleteView
)

from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='book-home'),
    path('listApp/<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('listApp/new/', BooksCreateView.as_view(), name='book-create'),
    path('listApp/<int:pk>/update', BooksUpdateView.as_view(), name='book-update'),
    path('listApp/<int:pk>/delete', BooksDeleteView.as_view(), name='book-delete'),
    path('listApp/apitest/', views.call_api_view, name='api')

]
