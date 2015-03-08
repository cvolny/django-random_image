from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from .models import Image
from .views import ExcludeRandomDetailView, ExcludeContextDetailView


urlpatterns = patterns('',
    url(r'(?P<pk>\d+)$', ExcludeContextDetailView.as_view(model=Image, exclude_name="previous"), name='image_detail'),
    url(r'^$', ExcludeRandomDetailView.as_view(model=Image, exclude_name="previous"), name='image_random'),
)
