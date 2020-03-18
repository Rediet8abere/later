from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.template import loader
from .models import Books
from django.shortcuts import get_object_or_404, render
import requests

booklist = [
    {
    'author_first_name':'Toni',
    'author_last_name':'Morrison',
    'book_title': 'Beloved',
    'list_pub_date':'March 16 2020'
    },
    {
    'author_first_name':'Haruki',
    'author_last_name':'Murakami',
    'book_title': '1Q84',
    'list_pub_date':'March 16 2020'
    }
]

def index(request):
    context = {
        'booklist': Books.objects.all()
    }
    return render(request, 'listApp/index.html', context)

class BooksListView(ListView):

    model = Books
    template_name = 'listApp/index.html'
    context_object_name = 'booklist'
    ordering = ['-list_pub_date']

class BooksDetailView(DetailView):

    model = Books

class BooksCreateView(CreateView):
    model = Books
    fields = ['author_name','book_title']

    def form_vaild(self, form):
        return super().form_vaild(form)

    # def get(self, request):
    #     pass


class BooksUpdateView(UpdateView):
    model = Books
    fields = ['author_name', 'book_title']

    def form_vaild(self, form):
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'
