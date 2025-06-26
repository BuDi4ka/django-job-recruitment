from django.contrib import admin
from django.urls import path, include

from application_tracking.views import list_adverts

urlpatterns = [
    path("", list_adverts, name="home"),
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("adverts/", include("application_tracking.urls")),
]
