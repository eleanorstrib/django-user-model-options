from django.conf import settings
from django.conf.urls import url
from . import views

url_patterns = [
    url(r'^$', views.home, name='index'),
]
