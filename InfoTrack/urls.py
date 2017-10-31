from django.conf.urls import url

from . import views


urlpatterns = [
    # or you can make it views.home, name = "home" and make corresponding change in views.py
     url(r'^$', views.index, name='index'),
     
]
