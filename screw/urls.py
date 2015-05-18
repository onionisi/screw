from django.conf.urls import patterns, include, url
from django.contrib import admin
import screw.index

urlpatterns = patterns('',
    url(r'^$', screw.index.index, {'template': 'index.html'}, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^good/', include('screw.app.good.urls')),
)
