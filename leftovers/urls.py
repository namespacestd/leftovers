from django.conf.urls import patterns, include, url
from leftovers.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index),
    url(r'^add_avaliability', scheduler),
    url(r'^add_schedule', add_schedule), 
	url (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    #url(r'^post.*', post_page),
    # Examples:
    # url(r'^$', 'leftovers.views.home', name='home'),
    # url(r'^leftovers/', include('leftovers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
