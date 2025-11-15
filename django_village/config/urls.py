from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic import RedirectView

from django_village.urls import urlpatterns as village_urlpatterns


urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("django_village/dist/favicon/favicon.ico")),
    ),
    # The "django_village/" prefix is here because this site is deployed as doc on
    # https://numerique-gouv.github.io/django_village/
    path("admin/", admin.site.urls),
    path("django_village/", include("example_village.urls")),
]
urlpatterns += village_urlpatterns
urlpatterns += [
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
