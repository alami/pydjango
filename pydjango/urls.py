"""pydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse

from app.views import hello_view, test_view, home_view, contact_view, since_view

class DataConverter:
    redux = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view, name='hello'), ##http://127.0.0.1:8000/hello?name=Alisher
    path('test33/', test_view, name='test'),  ##http://127.0.0.1:8000/test33/
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('since/<date>/', since_view, name='since'),
]

print(reverse('hello'))
