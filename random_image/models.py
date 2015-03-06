from urllib.parse import urlparse
from random import randint
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class RandomManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        if count < 1:
            raise RandomImage.DoesNotExist()
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class RandomImage(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=512)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = RandomManager()

    def __str__(self):
        return u'%s' % self.title

    def url_site(self):
        return urlparse(self.url).hostname
