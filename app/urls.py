from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^price/$', views.ShowPrice, name='showprice'),
    url(r'^form/$', views.ShowForm, name='showform'),
    url(r'^$', views.main, name='main'),
]