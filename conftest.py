import pytest

from django.test.client import Client
from django.contrib.auth.hashers import make_password

from accounts.models import User


@pytest.fixture 
def client():
    return Client()


@pytest.fixture
def user_instance(db):
    return User.objects.create(
        email="randomabc@gmail.com",
        password=make_password("randompassword")
    )


@pytest.fixture
def auth_user_password() -> str:
    """ Returns the password needed for auth """
    return "randompassword"