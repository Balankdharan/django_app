#from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

app_name='articles'


urlpatterns = [

    path('/',views.article_list, name="list"),
    path('/create',views.article_create, name="create"),
    re_path(r'^/(?P<slug>[\w-]+)/$', views.article_details, name="details" ),
    #url(r'^(?P<slug>[\w-]+)/$', views.article_details)
]
