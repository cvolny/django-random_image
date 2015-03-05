from django.contrib import admin
from .models import RandomImage


class RandomImageAdmin(admin.ModelAdmin):
    fields = ['title', 'file']



admin.site.register(RandomImage, RandomImageAdmin)
