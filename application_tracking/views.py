from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import JobAdvertForm
from .models import JobAdvert


def create_advert(request: HttpRequest):
    form = JobAdvertForm(request.POST or None)

    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.created_by = request.user
        instance.save()

        messages.success(request, "Advert created. You can receive applications")

    context = {
        "form": form,
        "title": "Create a new advert"
    }
    
    return render(request, "create_advert.html", context)


def list_adverts():
    pass


def get_advert():
    pass


def delete_advert():
    pass


def apply():
    pass


def my_applications():
    pass


def my_jobs():
    pass
