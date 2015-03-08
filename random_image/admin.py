from django.conf import settings
from django.core import urlresolvers
from django.contrib import admin
from .models import Image


CHANGE_LIST_TEMPLATE = admin.ModelAdmin.change_list_template
CHANGE_FORM_TEMPLATE = admin.ModelAdmin.change_form_template
if settings.USE_COLORBOX:
    CHANGE_LIST_TEMPLATE = 'admin/colorbox_change_list.html'
    CHANGE_FORM_TEMPLATE = 'admin/colorbox_change_form.html'


class ImageAdmin(admin.ModelAdmin):
    change_list_template = CHANGE_LIST_TEMPLATE
    change_form_template = CHANGE_FORM_TEMPLATE
    fields = ('id', 'user_link', 'title', 'caption', 'url',)
    readonly_fields = ('id', 'user_link', 'caption_link',)
    list_display = ('id', 'title', 'caption_link', 'user_link', 'timestamp', 'clickable_url',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def caption_link(self, obj):
        return '<a href="%s">%s</a>' % (
            urlresolvers.reverse('random_image:image_detail', args=(obj.id,)),
            obj.caption,
        )
    caption_link.allow_tags = True
    caption_link.short_description = "Caption"

    def user_link(self, obj):
        return '<a href="%s">%s</a>' % (
            urlresolvers.reverse('admin:auth_user_change', args=(obj.user.id,)),
            obj.user
        )
    user_link.allow_tags = True
    user_link.short_description = "User"

    def clickable_url(self, obj):
        return ((
            '<a class="colorbox" href="%s" title="%s" '
            + 'data-pk="%s" data-gallery="change_list_gallery" target="_blank">%s</a>')
            % (obj.url, obj.title, obj.id, obj.url)
        )
    clickable_url.allow_tags = True
    clickable_url.short_description = "Url"

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)
