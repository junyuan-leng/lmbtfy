from django.conf.urls import patterns, include, url
from my_site.views import search,visited

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^search/$',search),
                       ('^visited/',visited),
    # Examples:
    # url(r'^$', 'my_site.views.home', name='home'),
    # url(r'^my_site/', include('my_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
