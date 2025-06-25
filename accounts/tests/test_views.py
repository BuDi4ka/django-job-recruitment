import pytest

from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.hashers import check_password
from django.contrib.messages import get_messages
from django.contrib.auth import get_user

from accounts.models import PendingUser, User

pytestmark = pytest.mark.django_db


def test_register_user(client: Client):
    url = reverse("register")
    request_data = {"email": "abc@gmail.com", "password": "123456789"}
    response = client.post(url, request_data)
    assert response.status_code == 200
    pending_user = PendingUser.objects.filter(email=request_data["email"]).first()
    assert pending_user
    assert check_password(request_data["password"], pending_user.password)

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "success"
    assert "Verification code has been sent to" in str(messages[0])


def test_register_user_duplicate_email(client: Client, user_instance):
    url = reverse("register")
    request_data = {
        "email": user_instance.email,
        "password": "abc",
    }
    response = client.post(url, request_data)
    assert response.status_code == 302
    assert response.url == reverse("register")

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "error"
    assert "Email already exists on the platform" in str(messages[0])


def test_verify_account_valid_code(client: Client):
    pending_user = PendingUser.objects.create(
        email="abc@gmail.com", verification_code="5555", password="randompassword"
    )
    url = reverse("verify-account")
    request_data = {"email": pending_user.email, "code": pending_user.verification_code}
    response = client.post(url, request_data)
    assert response.status_code == 302
    assert response.url == reverse("home")
    user = get_user(response.wsgi_request)
    assert user.is_authenticated


def test_verify_account_invalid_code(client: Client):
    pending_user = PendingUser.objects.create(
        email="abc@gmail.com", verification_code="5555", password="randompassword"
    )
    url = reverse("verify-account")
    request_data = {"email": pending_user.email, "code": "invalidcode"}
    response = client.post(url, request_data)
    assert response.status_code == 400
    assert User.objects.count() == 0

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "error"
    assert "Invalid or expired verification code" in str(messages[0])


def test_login_valid_credentials(client: Client, user_instance, auth_user_password):
    url = reverse("login")
    request_data = {"email": user_instance.email, "password": auth_user_password}
    response = client.post(url, request_data)
    assert response.status_code == 302
    assert response.url == reverse("home")

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "success"


def test_login_invalid_credentials(client: Client, user_instance):
    url = reverse("login")
    request_data = {"email": user_instance.email, "password": "dejdediedie"}
    response = client.post(url, request_data)
    assert response.status_code == 302
    assert response.url == reverse("login")

    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert messages[0].level_tag == "error"
    assert "Invalid credentials" in str(messages[0])


