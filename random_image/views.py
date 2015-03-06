from django.shortcuts import render
from django.views import generic
from .models import Image
from django.http import Http404


TEMPLATE_VIEW_IMAGE = 'random_image/view_image.html'


class IndexDirectView(generic.DetailView):
    def get_object(self, queryset=None):
        try:
            return Image.objects.random()
        except Image.DoesNotExist:
            raise Http404
