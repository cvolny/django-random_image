from django.conf.urls import patterns, url
from .views import index, DirectView


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)$', DirectView.as_view(), name='direct'),
    url(r'^$', index, name='index'),
)
