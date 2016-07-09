from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pagecheck/(?P<pk>[0-9A-Za-z]*)$', views.PageCheckView.as_view(), name='page_check'),
    url(r'^(?P<pk>[0-9A-Za-z]+)/uploadimg$',views.uploadimg, name='uploadimg'),
    url(r'^(?P<page_id>[0-9A-Za-z]+)/$', views.page_detail, name='page_detail'),
    url(r'^(?P<page_id>[0-9A-Za-z]+)/modify$', views.page_modify, name='page_modify'),
    url(r'^charactercheck/(?P<char>.*)', views.character_check, name='character_check'),
    url(r'^set_correct$', views.set_correct, name='set_correct'),
]