from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from application_tracking.views import list_adverts

urlpatterns = [
    path("", list_adverts, name="home"),
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("adverts/", include("application_tracking.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
