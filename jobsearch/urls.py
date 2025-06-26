from django.contrib import admin
from django.urls import path, include

from accounts.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("adverts/", include("application_tracking.urls")),
]
