from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages, auth
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string

from datetime import datetime, timezone

from .models import User, PendingUser
from common.tasks import send_email


def home(request: HttpRequest):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        email: str = request.POST["email"]
        password: str = request.POST["password"]
        cleaned_email = email.lower()

        if User.objects.filter(email=cleaned_email).exists():
            messages.error(request, "Email already exists on the platform")
            return redirect("register")
        
        else:
            verification_code = get_random_string(10)
            PendingUser.objects.update_or_create(
                email=cleaned_email,
                defaults={
                    "password": make_password(password),
                    "verification_code": verification_code,
                    "created_at": datetime.now(timezone.utc)
                }
            )
            send_email(
                "Verify your account",
                [cleaned_email], 
                "emails/email_verification_template.html",
                context= {
                    "code": verification_code
                }
            )
            messages.success(request, f"Verification code has been sent to {cleaned_email}")
            return render(request, "verify_account.html")

    else:
        return render(request, "register.html")
    

def verify_account(request: HttpRequest):
    if request.method == "POST":
        code: str = request.POST["code"]
        email: str = request.POST["email"]

        pending_user = PendingUser.objects.filter(
            verification_code = code, email = email
        ).first()
        if pending_user and pending_user.is_valid:
            user = User.objects.create(
                email=pending_user.email,
                password=pending_user.password
            )
            pending_user.delete()
            auth.login(request, user)
            messages.success(request, "Account verified. You are now logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid or expired verification code")
            return render(request, "verify_account.html", status=400)
