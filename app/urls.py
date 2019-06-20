from django.conf.urls import url
from . import views

app_name ='app'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^madion/$',views.MadionListView.as_view(),name='madion'),
    url(r'^madion/(?P<pk>[0-9A-Za-z-]+)/$',views.MadionDetailView.as_view(),name='madion-detail'),


]
