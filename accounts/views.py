from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string

from datetime import datetime, timezone

from .models import User, PendingUser


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
            # send_email()
            messages.success(request, f"Verification code has been sent to {cleaned_email}")
            return render(request, "verify_account.html")

    else:
        return render(request, "register.html")
