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
import json
# import json as simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt

class BooksListView(ListView):

    model = Books
    template_name = 'listApp/index.html'
    context_object_name = 'booklist'
    ordering = ['-list_pub_date']

class BooksDetailView(DetailView):

    model = Books

class BooksCreateView(CreateView):
    model = Books
    fields = ['book_title_or_author_name']

    def form_vaild(self, form):
        return super().form_vaild(form)

    def post(self, request):
        if request.method == 'POST':
            print("preparing to post")
            print(request.body)
            jsonData = json.loads(request.body)
            print("loading .....")
            print(jsonData)
            book = Books(book_title_or_author_name=jsonData)
            book.save(force_insert=True)
            return HttpResponse(jsonData)
            # return HttpResponseRedirect(reverse('listApp:book-home'))

class BooksUpdateView(UpdateView):
    model = Books
    fields = ['book_title_or_author_name']

    def form_vaild(self, form):
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'
