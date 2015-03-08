from urllib.parse import urlparse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


BRIEF_LENGTH = 75


class Image(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.TextField(verbose_name="Description")
    cite = models.URLField(max_length=512, verbose_name="Citation URL")
    image = models.URLField(max_length=512, verbose_name="Image URL")
    user = models.ForeignKey(User, verbose_name="Submitted by")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Submitted on")

    def __str__(self):
        return u'%s' % self.title

    def cite_site(self):
        return urlparse(self.cite).hostname

    def body_brief(self):
        if BRIEF_LENGTH < len(self.body):
            return self.body[:BRIEF_LENGTH - 3] + "..."
        return self.body

    def get_absolute_url(self):
        return reverse('random_image:image_detail', args=[str(self.id)])
