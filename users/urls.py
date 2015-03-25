from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name='login'),
	url(r'^login_validate/$', views.login_validate, name='login_validate'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register_validate/$', views.register_validate, name='register_validate'),
	url(r'^home/$', views.home, name='home'),		
)

urlpatterns += staticfiles_urlpatterns()