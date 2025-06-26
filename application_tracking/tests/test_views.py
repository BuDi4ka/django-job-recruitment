from django.test.client import Client
from django.urls import reverse

from .factories import JobAdvertFactory, fake


def test_list_adverts(client: Client, user_instance):
    JobAdvertFactory.create_batch(20, created_by=user_instance, deadline=fake.future_date())
    JobAdvertFactory.create_batch(5, created_by=user_instance, deadline=fake.past_date())

    url = reverse("home")
    response = client



def test_retreive_advert():
    pass


def test_create_advert():
    pass


def test_delete_advert():
    pass


def test_edit_advert():
    pass


def test_my_applications():
    pass


def test_my_jobs():
    pass


def test_apply_job():
    pass
