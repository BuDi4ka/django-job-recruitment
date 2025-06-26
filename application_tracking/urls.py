from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.create_advert, name="create-advert"),
    path("my-applications/", views.my_applications, name="my-applications"),
    path("my-jobs/", views.my_jobs, name="my-jobs"),
    path("<uuid:advert_id>/", views.get_advert, name="job-advert"),
    path("<uuid:advert_id>/apply/", views.apply, name="apply-job"),
    path("<uuid:advert_id>/applications/", views.advert_applications, name="job-applications"),
    path("<uuid:advert_id>/update/", views.update_advert, name="update-advert"),
    path("<uuid:advert_id>/delete/", views.delete_advert, name="delete-advert"),
]
