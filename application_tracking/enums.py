from django.db import models


class EmploymentType(models.TextChoices):
    FULL_TIME = "full_time", "Full Time"
    PART_TIME = "part_time", "Part Time"
    CONTRACT = "contract", "Contract"


class ExperienceLevel(models.TextChoices):
    ENTRY = "entry", "Entry Level"
    MID = "mid", "Mid Level"
    SENIOR = "senior", "Senior"


class JobType(models.TextChoices):
    ONSITE = "onsite", "On-site"
    HYBRID = "hybrid", "Hybrid"
    REMOTE = "remote", "Remote"


class ApplicationStatus(models.TextChoices):
    APPLIED = ("applied", "Applied")
    REJECTED = ("rejected", "Rejected")
    INTERVIEW = ("interview", "Interview")
