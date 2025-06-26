import factory
from faker import Faker

from application_tracking.models import JobAdvert


fake = Faker()


class JobAdvertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobAdvert

    title = fake.job()
    company_name = fake.company()
    description = fake.sentence()
    skills = "Python, Django"
    deadline = fake.date()
