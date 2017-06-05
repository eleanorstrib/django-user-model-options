from django.conf.urls import url, include
from . import views

print(views)

urlpatterns = [
    url(r'^$', views.home, name='home')
]
