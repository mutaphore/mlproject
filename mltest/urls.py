from django.conf.urls import patterns, url
from mltest import views

urlpatterns = patterns('',
	url(r'^$', views.indexView, name='Index'),
	url(r'^results/$', views.resultsView, name='Results'),
	url(r'^results/(?P<inputId>\d+)/$', views.resultsView, name='ResultsWithId'),)
