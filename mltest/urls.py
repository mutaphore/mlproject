from django.conf.urls import patterns, url
from mltest import views

urlpatterns = patterns('',
	url(r'^$', views.indexView, name='index'),
	url(r'^results/(?P<inputId>\d+)/$', views.resultsView, name='results'),)