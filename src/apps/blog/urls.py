from django.conf.urls import url

from .views import index, articles


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', articles, name='articles'),
]
