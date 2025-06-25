from django.urls import path

from . import views

urlpatterns = [

    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("verify-account/", views.verify_account, name="verify-account")
]
