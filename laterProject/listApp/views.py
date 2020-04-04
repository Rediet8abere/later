from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.template import loader
from .models import Books
from django.shortcuts import get_object_or_404, render, redirect
import requests
import json
# import json as simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class HomeView(TemplateView):
    template_name = "listApp/home.html"

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
    # template_name = 'listApp/books.html'
    print("In create view")

    def form_vaild(self, form):
        return super().form_vaild(form)

    def post(self, request):
        print("posting data to the server")
        if request.method == 'POST':
            book = Books(book_title_or_author_name=request.POST['title'])
            print(request.POST['title'])
            book.save(force_insert=True)
            return  HttpResponseRedirect("/listApp/books")
            # return redirect('books')
            # context = {'response': data["data"]}
            # return render(request, 'listApp/index.html', {'booklist': book})


class BooksUpdateView(UpdateView):
    model = Books
    fields = ['book_title_or_author_name']

    def form_vaild(self, form):
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'




def music_api_view(request):

    if request.method == 'GET':
        context = {'list_name': 'Music Club'}
        return render(request, 'listApp/searchList.html', context)

    if request.method == 'POST':
        search_term = request.POST['querystring']
        print(type(search_term))
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        querystring =  {"q":search_term}
        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "197b9992b3mshf84e47cf0693477p123b73jsnb27522c04ca3"
            }
        response = requests.request("GET", url, headers=headers, params=querystring )
        data = response.json()
        context = {'response': data["data"], 'list_name': 'Music Club'}

        # return render(request, 'listApp/music.html', context)
        return render(request, 'listApp/searchList.html', context)

def book_api_view(request):
    url = "https://www.googleapis.com/books/v1/volumes?q=beloved"
    # querystring =  {"q":"Beyonc%C3%A9"}
    # data.items[i].volumeInfo.title
    if request.method == 'GET':
        context = {'list_name': 'Book World'}
        return render(request, 'listApp/searchList.html', context)

    if request.method == 'POST':
        search_term = request.POST['querystring']
        response = requests.request("GET", f'https://www.googleapis.com/books/v1/volumes?q={search_term}')


        data = response.json()
        context = {'response': data['items'], 'list_name': 'Book World'}

        return render(request, 'listApp/searchList.html', context)

    return render(request, 'listApp/searchList.html')
