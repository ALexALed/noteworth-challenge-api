from django.test import TestCase

from providers.tests.factories import EmployeeFactory

from providers.serializers import EmployeeSerializer
from providers.models import Clinic, Title, Employee


class EmployeeSerializerTestCase(TestCase):
    def test_no_clinic_duplication(self):

        test_clinic_name = "Noteworth General"
        data = [
            {
                "name_given": "Jasper",
                "name_family": "Mueller",
                "title": "Dr.",
                "clinic": test_clinic_name,
            },
            {
                "name_given": "Guy",
                "name_family": "Bright",
                "title": "PA",
                "clinic": test_clinic_name,
            },
        ]

        employees = EmployeeSerializer(data=data, many=True)
        assert employees.is_valid()
        employees.save()
        assert Clinic.objects.count() == 1
        assert Clinic.objects.first().name == test_clinic_name

    def test_no_titles_duplication(self):

        test_title_name = "Dr."
        data = [
            {
                "name_given": "Jasper",
                "name_family": "Mueller",
                "title": test_title_name,
                "clinic": "Noteworth General",
            },
            {
                "name_given": "Guy",
                "name_family": "Bright",
                "title": test_title_name,
                "clinic": "Noteworth General",
            },
        ]

        employees = EmployeeSerializer(data=data, many=True)
        assert employees.is_valid()
        employees.save()
        assert Title.objects.count() == 1
        assert Title.objects.first().name == test_title_name

    def test_no_employees_duplication(self):

        test_title_name = "Dr."
        data = [
            {
                "name_given": "Jasper",
                "name_family": "Mueller",
                "title": "Dr.",
                "clinic": "Noteworth General",
            },
            {
                "name_given": "Jasper",
                "name_family": "Mueller",
                "title": "Dr.",
                "clinic": "Noteworth General",
            },
        ]

        employees = EmployeeSerializer(data=data, many=True)
        assert employees.is_valid()
        employees.save()
        assert Employee.objects.count() == 1
