from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.template import loader
from .models import Books, Musics
from django.shortcuts import get_object_or_404, render, redirect
import requests
import json
# import json as simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class HomePageView(TemplateView):
    # template_name = "listApp/home.html"
    template_name = "listApp/homepage.html"

class HomeView(TemplateView):
    template_name = "listApp/home.html"
    # template_name = "listApp/about.html"

class BooksListView(ListView):
    # print("BooksListView")
    model = Books
    template_name = 'listApp/booklist.html'
    context_object_name = 'booklist'
    ordering = ['-list_pub_date']
    paginate_by = 6

class MusicListView(ListView):
    # print("MusicListView")
    model = Musics
    template_name = 'listApp/musiclist.html'
    context_object_name = 'musiclist'
    ordering = ['-list_pub_date']

class BooksDetailView(DetailView):
    model = Books

class BooksCreateView(CreateView):
    model = Books
    fields = ['book_title']
    # template_name = 'listApp/books.html'
    # print("BooksCreateView")

    def form_vaild(self, form):
        form.instance.author = self.request.user
        return super().form_vaild(form)

    def post(self, request):
        print("posting data to the server")
        if request.method == 'POST':
            book = Books(book_title=request.POST['title'], author_name=request.POST['author'], image=request.POST['image'], description = request.POST['desc'])
            print(request.POST['desc'])
            book.save(force_insert=True)
            return  HttpResponseRedirect("/listApp/books")
            # return redirect('books')
            # context = {'response': data["data"]}
            # return render(request, 'listApp/index.html', {'booklist': book})

class MusicCreateView(CreateView):
    model = Musics
    fields = ['artist']
    # template_name = 'listApp/books.html'
    # print("MusicCreateView")

    def form_vaild(self, form):
        form.instance.author = self.request.user
        return super().form_vaild(form)

    def post(self, request):
        # print("posting data to the server")
        if request.method == 'POST':
            music = Musics(artist=request.POST['title'])
            print(request.POST['title'])
            music.save(force_insert=True)
            return  HttpResponseRedirect("/listApp/music")
            # return redirect('books')
            # context = {'response': data["data"]}
            # return render(request, 'listApp/index.html', {'booklist': book})

class BooksUpdateView(UpdateView):
    model = Books
    fields = ['book_title_or_author_name']

    def form_vaild(self, form):
        form.instance.author = self.request.user
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'


def music_api_view(request):
    # print("music_api_view")
    if request.method == 'GET':
        # print("getting")
        context = {'list_name': 'Music Club', 'urlName' : 'music', 'viewlist' : 'music-list'}
        print('context: ', context)
        return render(request, 'listApp/searchList.html', context)

    if request.method == 'POST':
        # print("posting")
        search_term = request.POST['querystring']
        # print(type(search_term))
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        querystring =  {"q":search_term}
        headers = {
            'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
            'x-rapidapi-key': "197b9992b3mshf84e47cf0693477p123b73jsnb27522c04ca3"
            }
        response = requests.request("GET", url, headers=headers, params=querystring )
        data = response.json()
        context = {'response': data["data"], 'list_name': 'Music Club', 'urlName' : 'music', 'viewlist' : 'music-list'}

        # return render(request, 'listApp/music.html', context)
        return render(request, 'listApp/searchList.html', context)

def book_api_view(request):
    # print("hello there we are in bookApi")
    url = "https://www.googleapis.com/books/v1/volumes?q=beloved"
    # querystring =  {"q":"Beyonc%C3%A9"}
    # data.items[i].volumeInfo.title
    if request.method == 'GET':
        # print("getting")
        context = {'list_name': 'Book World', 'urlName' : 'books', 'viewlist' : 'book-list'}
        return render(request, 'listApp/searchList.html', context)

    if request.method == 'POST':
        # print("posting")
        search_term = request.POST['querystring']
        response = requests.request("GET", f'https://www.googleapis.com/books/v1/volumes?q={search_term}')


        data = response.json()
        context = {'response': data['items'], 'list_name': 'Book World', 'urlName' : 'music', 'viewlist' : 'book-list'}

        return render(request, 'listApp/searchList.html', context)

    # return render(request, 'listApp/searchList.html')

def about(request):
    return render(request, 'listApp/about.html', {'title': 'About'})