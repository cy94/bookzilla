from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from books import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)

urlpatterns += staticfiles_urlpatterns()