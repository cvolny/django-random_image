from django.shortcuts import render
from django.views import generic
from .models import RandomImage


TEMPLATE_VIEW_IMAGE = 'random_image/view_image.html'


def index(request):
    img = RandomImage.objects.random()
    return render(request, TEMPLATE_VIEW_IMAGE, {'object': img})


class DirectView(generic.DetailView):
    template_name = TEMPLATE_VIEW_IMAGE
    model = RandomImage
