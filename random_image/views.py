from abc import ABCMeta, abstractmethod
from django.views.generic import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.http import Http404
from django.db.models import Count
from random import randint


class ExcludeMixin(SingleObjectMixin):
    __metaclass__ = ABCMeta
    exclude_name = "exclude"

    @abstractmethod
    def get_storage(self):
        pass

    def get_queryset(self):
        queryset = super(ExcludeMixin, self).get_queryset()
        pk = self.get_storage().get(self.exclude_name, False)
        if pk:
            queryset = queryset.exclude(pk=pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ExcludeMixin, self).get_context_data(**kwargs)
        context["exclude"] = {
            'name': self.exclude_name,
            'id': self.get_storage().get(self.exclude_name, "")
        }
        return context


class CookieExcludeMixin(ExcludeMixin):

    def get_storage(self):
        return self.request.COOKIES


class RandomMixin(SingleObjectMixin):

    @classmethod
    def get_random(cls, queryset):
        count = queryset.aggregate(count=Count('id'))['count']
        if count < 1:
            raise queryset.model.DoesNotExist()
        i = randint(0, count - 1)
        return queryset.all()[i]

    def get_object(self, queryset=None):
        try:
            if not queryset:
                queryset = self.get_queryset()
            return RandomMixin.get_random(queryset)
        except self.model.DoesNotExist:
            raise Http404


class ExcludeRandomDetailView(CookieExcludeMixin, RandomMixin, DetailView):
    pass