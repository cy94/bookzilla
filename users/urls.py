from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name='login'),
	url(r'^login_validate/$', views.login_validate, name='login_validate'),
	url(r'^register/$', views.register, name='register'),
	# no slash after validate for AJAX
	url(r'^register/register_validate$', views.register_validate, name='register_validate'),
	url(r'^home/$', views.home, name='home'),
	url(r'^test/$', views.test, name='test'),
	url(r'^logout/$', views.logout, name='logout'),		
)

urlpatterns += staticfiles_urlpatterns()