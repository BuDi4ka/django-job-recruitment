from django.shortcuts import render, get_object_or_404, redirect
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

        return redirect(instance.get_absolute_url())

    context = {
        "job_advert_form": form,
        "title": "Create a new advert",
        "btn_text": "Create advert"
    }
    
    return render(request, "create_advert.html", context)


def list_adverts():
    pass


def get_advert(request: HttpRequest, advert_id):
    job_advert = get_object_or_404(JobAdvert, pk=advert_id)
    context = {
        "job_advert": job_advert
    }
    return render(request, "advert.html", context)


def delete_advert():
    pass


def apply():
    pass


def my_applications():
    pass


def my_jobs():
    pass
