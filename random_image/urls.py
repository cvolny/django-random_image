from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from .models import Image
from .views import IndexDirectView


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)$', DetailView.as_view(model=Image), name='direct'),
    url(r'^$', IndexDirectView.as_view(), name='index'),
)
