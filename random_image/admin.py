from django.conf import settings
from django.contrib import admin
from .models import RandomImage


IMG_URL_ATTRS = 'target="_blank" data-pk="%s" data-title="%s"'
CHANGE_LIST_TEMPLATE = admin.ModelAdmin.change_list_template
CHANGE_FORM_TEMPLATE = admin.ModelAdmin.change_form_template
if settings.USE_LIGHTBOX:
    IMG_URL_ATTRS = 'data-lightbox="%s" data-title="%s"'
    CHANGE_LIST_TEMPLATE = 'admin/lightbox_change_list.html'
    CHANGE_FORM_TEMPLATE = 'admin/lightbox_change_form.html'


class RandomImageAdmin(admin.ModelAdmin):
    change_list_template = CHANGE_LIST_TEMPLATE
    change_form_template = CHANGE_FORM_TEMPLATE
    fields = ('id', 'title', 'url')
    readonly_fields = ('id',)
    list_display = ('title', 'timestamp', 'clickable_url')

    def clickable_url(self, obj):
        url_attrs = IMG_URL_ATTRS % (obj.id, obj.title)
        return '<a href="%s" %s>%s</a>' % (obj.url, url_attrs, obj.url)
    clickable_url.allow_tags = True

    class Meta:
        model = RandomImage


admin.site.register(RandomImage, RandomImageAdmin)
