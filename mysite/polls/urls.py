from django.conf.urls import url, include
from . import views

urlpatterns = [
   url(r'^$', views.RestView.get, name='get'),
   url(r'^add_todo/$', views.RestView.post, name='post'),
   url(r'^edit_todo/([0-9]+)$', views.RestView.put, name='put'),
   url(r'^update_todo/([0-9]+)$', views.RestView.update, name='put'),
   url(r'^delete/([0-9]+)$', views.RestView.delete, name='delete'),
   url(r'^all/$', views.RestView.all, name='all'),
   url(r'^checked/$', views.RestView.checked, name='checked'),
   url(r'^unchecked/$', views.RestView.unchecked, name='unchecked'),
   url(r'^off/$', views.RestView.offAll, name='offAll'),
   url(r'^on/$', views.RestView.onAll, name='onAll'),
   url(r'^del/$', views.RestView.delAll, name='dell'),
]

urlpatterns += [

]
