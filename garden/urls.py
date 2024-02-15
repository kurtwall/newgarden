from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from garden import settings

urlpatterns = (([
    path("admin/", admin.site.urls),
    path("", include('plants.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
