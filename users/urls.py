from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users import views

urlpatterns = patterns('',
	url(r'^home/$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),		

	# books module
	url(r'^books/', include('books.urls', namespace='books')),
	# bookrequests module
	url(r'^requests/', include('bookrequests.urls', namespace='requests')),
)

urlpatterns += staticfiles_urlpatterns()