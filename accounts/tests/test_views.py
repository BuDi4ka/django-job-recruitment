import pytest

from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.hashers import check_password
from django.contrib.messages import get_messages

from accounts.models import PendingUser

pytestmark = pytest.mark.django_db

def test_register_user(client: Client):
    url = reverse("register")
    request_data = {
        "email": "abc@gmail.com",
        "password": "123456789"
    }
    response = client.post(url, request_data)
    assert response.status_code == 200
    pending_user = PendingUser.objects.filter(
        email=request_data["email"]
    ).first()
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


# def test_verify_account_valid_code():
#     pass


# def test_verify_account_invalid_code():
#     pass


# def test_login_invalid_credentials():
#     pass
