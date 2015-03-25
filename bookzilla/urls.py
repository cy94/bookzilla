from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bookzilla import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bookzilla.views.index', name='index'),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^about/', views.about, name='about' ),
    url(r'^contact/', views.contact, name='contact'),
  	
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()


