from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<slug>[\w-]+)/$', views.article, name='article'),
    url(r'^score/(?P<series_id>[0-9]+)/(?P<match_id>[0-9]+)/$', views.score, name='score'),
    url(r'^fixtures/$', views.fixtures, name='fixtures'),
    url(r'^create_post/$', views.create_post, name='create_poll'),
    url(r'^search/$', views.search, name='search'),
    url(r'^featured-news/$', views.featured_news, name='feature'),
]
