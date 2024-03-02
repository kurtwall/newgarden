from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

from garden import settings
from plants import views

# for django-recurrence
js_info_dict = {
    'packages': ('recurrence', ),
}

urlpatterns = (([
    path("admin/", admin.site.urls),
    path("", include('plants.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

