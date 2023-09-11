from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from blogs.views import RobotsView
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("u8DqbcHRCKJdhJjVj9SBukLzJwQ8jhaNaGveDfMA/", admin.site.urls),
    path("V3UN6NQBg7tLzWw93PFBTUXMnq45PvNQyE9q0dUO/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path('sitemap.xml', sitemap),
    path('robots.txt', RobotsView.as_view()),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
