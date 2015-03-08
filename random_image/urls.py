from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from .models import Image
from .views import ExcludeRandomDetailView


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)$', DetailView.as_view(model=Image), name='image_detail'),
    url(r'^$', ExcludeRandomDetailView.as_view(model=Image, exclude_name="previous"), name='image_random'),
)
