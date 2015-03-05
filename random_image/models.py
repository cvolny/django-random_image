import os
import uuid
from random import randint
from django.db import models
from django.db.models import Count
from sorl import thumbnail


class RandomManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


def upload_to_filename(instance, filename):
    path = "random"
    fn, ext = os.path.splitext(filename)
    ofn = str(uuid.uuid4()) + ext
    return os.path.join(path, ofn)


class RandomImage(models.Model):
    title = models.CharField(max_length=255)
    height = models.IntegerField()
    width = models.IntegerField()
    file = thumbnail.ImageField(upload_to=upload_to_filename, height_field="height", width_field="width")
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = RandomManager()

    def __unicode__(self):
        return self.title
