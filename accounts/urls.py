from django.urls import path

from . import views

urlpatterns = [

    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("verify-account/", views.verify_account, name="verify-account"),
    path("forgot-password/", views.send_password_reset_link, name="reset-password-via-email"),
    path("verify-password-reset-link/", views.verify_password_reset_link, name="verify-password-reset-link"),
]
