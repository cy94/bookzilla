from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bookrequests import views

urlpatterns = patterns('',
	url(r'^lent/$', views.lent_index, name='lent'),
	url(r'^borrowed/$', views.borrowed_index, name='borrowed'),
)

urlpatterns += staticfiles_urlpatterns()