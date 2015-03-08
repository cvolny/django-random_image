from django.contrib import admin
from django.db import models
from .models import Image


CHANGE_LIST_LINK = '<a href="{0}" title="{1}" data-gallery="{2}" class="colorbox {3}" target="_blank">{0}</a>'
CHANGE_FORM_LINK = '<a href="{0}" class="colorbox {1}" target="_blank">{0}</a>'


def get_verbose_name(model: models.Model, field_name):
    return model._meta.get_field(field_name).verbose_name


class ImageAdmin(admin.ModelAdmin):
    change_form_template = "admin/image_change_form.html"
    change_list_template = "admin/image_change_list.html"
    fields = ('id', 'view_link', 'title', 'body', 'cite', 'image', 'user', 'created',)
    readonly_fields = ('id', 'view_link', 'created')
    list_display = ('title', 'body_brief', 'cite_link', 'image_link', 'user', 'created',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def cite_link(self, obj):
        return CHANGE_LIST_LINK.format(obj.cite, obj.title, "change_list_citations", "iframe")
    cite_link.allow_tags = True
    cite_link.short_description = get_verbose_name(Image, "cite")

    def image_link(self, obj):
        return CHANGE_LIST_LINK.format(obj.image, obj.title, "change_list_images", "image")
    image_link.allow_tags = True
    image_link.short_description = get_verbose_name(Image, "image")

    def view_link(self, obj):
        return CHANGE_FORM_LINK.format(obj.get_absolute_url(), "iframe")
    view_link.allow_tags = True
    view_link.short_description = "View"

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)
