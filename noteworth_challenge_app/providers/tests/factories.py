import factory
import factory.fuzzy

from providers.models import Employee, Clinic, Title


class ClinicFactory(factory.django.DjangoModelFactory):

    name = factory.fuzzy.FuzzyText(length=100)

    class Meta:
        model = Clinic


class TitleFactory(factory.django.DjangoModelFactory):

    name = factory.fuzzy.FuzzyText(length=100)

    class Meta:
        model = Title


class EmployeeFactory(factory.django.DjangoModelFactory):

    title = factory.SubFactory(TitleFactory)
    clinic = factory.SubFactory(ClinicFactory)
    given_name = factory.fuzzy.FuzzyText(length=100)
    family_name = factory.fuzzy.FuzzyText(length=100)

    class Meta:
        model = Employee
