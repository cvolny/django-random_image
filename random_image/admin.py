from django.conf import settings
from django.core import urlresolvers
from django.contrib import admin
from .models import Image


IMG_URL_ATTRS = 'target="_blank" data-pk="%s" data-title="%s"'
CHANGE_LIST_TEMPLATE = admin.ModelAdmin.change_list_template
CHANGE_FORM_TEMPLATE = admin.ModelAdmin.change_form_template
if settings.USE_LIGHTBOX:
    IMG_URL_ATTRS = 'data-lightbox="%s" data-title="%s"'
    CHANGE_LIST_TEMPLATE = 'admin/lightbox_change_list.html'
    CHANGE_FORM_TEMPLATE = 'admin/lightbox_change_form.html'


class ImageAdmin(admin.ModelAdmin):
    change_list_template = CHANGE_LIST_TEMPLATE
    change_form_template = CHANGE_FORM_TEMPLATE
    fields = ('id', 'user_link', 'title', 'url',)
    readonly_fields = ('id', 'user_link', 'title_link',)
    list_display = ('id', 'title_link', 'user_link', 'timestamp', 'clickable_url',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def title_link(self, obj):
        return '<a href="%s">%s</a>' % (
            urlresolvers.reverse('random_image:direct', args=(obj.id,)),
            obj.title,
        )
    title_link.allow_tags = True
    title_link.short_description = "Title"

    def user_link(self, obj):
        return '<a href="%s">%s</a>' % (
            urlresolvers.reverse('admin:auth_user_change', args=(obj.user.id,)),
            obj.user
        )
    user_link.allow_tags = True
    user_link.short_description = "User"

    def clickable_url(self, obj):
        url_attrs = IMG_URL_ATTRS % (obj.id, obj.title)
        return '<a href="%s" %s>%s</a>' % (obj.url, url_attrs, obj.url)
    clickable_url.allow_tags = True
    clickable_url.short_description = "Url"

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)
