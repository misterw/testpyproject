from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testpyproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(auth_urls)),
)
