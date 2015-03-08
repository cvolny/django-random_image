from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=255)
    url = models.URLField(max_length=512)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s' % self.title

    def url_site(self):
        return urlparse(self.url).hostname
