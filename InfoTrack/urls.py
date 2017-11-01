from django.conf.urls import url
from . import views


urlpatterns = [
    # or you can make it views.home, name = "home" and make corresponding change in views.py
     #url(r'^$', views.index, name='index'),   
     url(r'^$', views.homepage, name='homepage'),  
     url(r'^clubinfo.html$', views.clubinfo, name='clubinfo'), 
     url(r'^courseinfo.html$', views.courseinfo, name='courseinfo'), 
     url(r'^freeride.html$', views.freeride, name='freeride'), 
     url(r'^privatetutor.html$', views.privatetutor, name='privatetutor'), 
     url(r'^rentinfo.html$', views.rentinfo, name='rentinfo') 
]
