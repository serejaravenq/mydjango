from django.conf.urls import url, include
from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
]

urlpatterns += [
    #url(r'^books/$', views.book_list, name='book_list'),
    #url(r'^books/create/$', views.book_create, name='book_create'),
     #url(r'^books/$', views.book_list, name='book_list'),
]
