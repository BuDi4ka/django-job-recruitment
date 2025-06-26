from django.forms import ModelForm
from django import forms

from .models import JobAdvert, JobApplication


class JobAdvertForm(ModelForm):
    class Meta:
        model = JobAdvert
        fields = [
            "title",
            "company_name",
            "employment_type",
            "experience_level",
            "job_type",
            "location",
            "description",
            "skills",
            "is_published",
            "deadline",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Job title", "class": "form-control"}
            ),
            "company_name": forms.TextInput(
                attrs={"placeholder": "Company name", "class": "form-control"}
            ),
            "employment_type": forms.Select(attrs={"class": "form-control"}),
            "experience_level": forms.Select(attrs={"class": "form-control"}),
            "job_type": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(
                attrs={"placeholder": "Location", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Job description",
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "skills": forms.TextInput(
                attrs={
                    "placeholder": "Skills (comma separated)",
                    "class": "form-control",
                }
            ),
            "deadline": forms.DateInput(
                attrs={"placeholdet": "Date", "class": "form-control", "type": "date"}
            ),
        }


class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "name",
            "email",
            "portfolio_url",
            "cv"
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Your name", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Your email", "class": "form-control"}
            ),
            "portfolio_url": forms.URLInput(
                attrs={"placeholder": "Portfolio URL", "class": "form-control"}
            ),
            "cv": forms.FileInput(
                attrs={"placeholder": "Portfolio URL", "class": "form-control", "accept": ".pdf, .docs, .doc"}
            ),
        }
