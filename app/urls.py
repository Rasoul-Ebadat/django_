from django.conf.urls import url
from . import views

app_name ='app'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),

    url(r'^madion/$',views.MadionListView.as_view(),name='madion'),
    url(r'^madion/(?P<pk>[0-9A-Za-z-]+)/$',views.MadionDetailView.as_view(),name='madion-detail'),

    url(r'^karshenas/$',views.KarshenasListView.as_view(),name='karshenas'),
    url(r'^karshenas/(?P<pk>[0-9A-Za-z-]+)/$',views.KarshenasDetailView.as_view(),name='karshenas-detail'),

    url(r'^shobe/$',views.ShobeListView.as_view(),name='shobe'),
    url(r'^shobe/(?P<pk>[0-9A-Za-z-]+)/$',views.ShobeDetailView.as_view(),name='shobe-detail'),

    url(r'^modiriat/$',views.ModiriatListView.as_view(),name='modiriat'),
    url(r'^modiriat/(?P<pk>[0-9A-Za-z-]+)/$',views.ModiriatDetailView.as_view(),name='modiriat-detail'),

]
