from django.http import HttpResponse
from django.template import loader
from .models import BookList


def index(request):
    latest_book_list = BookList.objects.order_by('-list_pub_date')[:5]
    template = loader.get_template('listApp/index.html')
    context = {
        'latest_book_list': latest_book_list,
    }
    return HttpResponse(template.render(context, request))
