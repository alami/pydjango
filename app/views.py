from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from django.conf import settings

def test_view(request):
    return HttpResponse(reverse('test'))

def home_view(request):
    return HttpResponse('Home from Django!  ')


def contact_view(request):
    msg = f'Contact email: {settings.CONTACT_EMAIL}'
    return HttpResponse(msg)

def hello_view(request):
    name = request.GET.get('name', 'Unknown')
    msg = f'Hi {name} from Django!  '
    return HttpResponse(msg)

# 127.0.0.1:8000/since/2020-01-01/
def since_view(request, date: datetime):
    daysi = (datetime.now() - date).days
    msg = f'Contact date: {daysi}'
    return HttpResponse(msg)


DATA = [str(i) for i in range(10000)]

## 127.0.0.1:8000/pagi?page=1
def pagi_view(request):
    paginator = Paginator(DATA, 10)
    page_number = int(request.GET.get('page', 7))
    page_obj = paginator.get_page(page_number)
    if page_obj.has_next():
        page_obj.next_page_number()
    if page_obj.has_previous():
        page_obj.previous_page_number()
    msg = '<br>'.join(page_obj.object_list)
    return HttpResponse(msg)

class User:
    def __init__(self,name):
        self.name = name
    def upper_name(self):
        return self.name.upper()
    def cut_name(self, n):
        return self.name[:n]


def data_view(request):
    u=User('Vova')
    context={
        'first_name':'Jake',
        'last_name':'The Dog',
        'user': u,
    }
    return render (request,'app/data.html',context={
        'first_name':'Jake',
        'last_name':'<h2>The Dog</h2>',
        'user': u,
        'marks':[2,4,6,8]
    })


