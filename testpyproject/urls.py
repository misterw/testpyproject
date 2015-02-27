from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testpyproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include(auth_urls)),
    url(r'^statistics/$', 'testpyproject.python_game.views.statistic_page', name="statistics_page"),
    url(r'^profile/$', 'testpyproject.python_game.views.profile_page', name="profile_page"),
    url(r'^news/$', 'testpyproject.news.views.news_page', name="news_page"),
    url(r'^news/(?P<news_id>[0-9]+)/', 'testpyproject.news.views.simple_news_page'),
    url(r'^profile/registration/$', 'testpyproject.python_game.views.register', name="registration_page"),
    url(r'^profile/save-result/$', 'testpyproject.python_game.views.save_result', name="save_result"),
)
