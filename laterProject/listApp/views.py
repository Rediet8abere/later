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
from django.http import JsonResponse

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

class BooksUpdateView(UpdateView):
    model = Books
    fields = ['book_title_or_author_name']

    def form_vaild(self, form):
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/'


url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring =  {"q":"Beyonc%C3%A9"}


headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "197b9992b3mshf84e47cf0693477p123b73jsnb27522c04ca3"
    }

def call_api_view(request):
    # api_call_response = requests.get('url')
    # json_response = api_call_response.json()
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(type(response))
    print(response.json())
    # res = json.loads(response)
    # print('res')
    # print(res)
    # print(json_response)
    # jsonData = json.loads(request.body)
    # json_string = json.dumps(response)
    # print("json string")
    # print(json_string)
    data = response.json()
    context = {'response': data["data"]}
    #
    # response = JsonResponse({'status':'false','message':message}, status=500)
    # print(response.text)
    # return JsonResponse(response)
    return render(request, 'listApp/music.html', context)

    if response.status_code == 200:
        return HttpResponse('Yay, it worked')
    else:
        return HttpResponse('Working progress')
