from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', 'django.contrib.flatpages.views.flatpage', {'url': '/about'}, name='about'),
    url(r'^', include("random_image.urls", app_name="random_image", namespace="random_image")),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
