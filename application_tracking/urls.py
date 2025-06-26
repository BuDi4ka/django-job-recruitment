from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.create_advert, name="create-advert"),
    path("my-applications", views.my_applications, name="my-applications"),
    path("<uuid:advert_id>/", views.get_advert, name="job-advert"),
    path("<uuid:advert_id>/apply/", views.apply, name="apply-job"),
]
