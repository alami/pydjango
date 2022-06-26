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




