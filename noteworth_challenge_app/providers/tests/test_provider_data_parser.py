from django.test import TestCase

from providers.models import Employee
from providers.provider_integration import ProviderDataParser


class ProviderDataParserTestCase(TestCase):
    def test_save_data_to_models(self):

        sample_data = [
            {
                "name_given": "Jasper",
                "name_family": "Mueller",
                "title": "Dr.",
                "clinic": "Noteworth General",
            },
            {
                "name_given": "Guy",
                "name_family": "Bright",
                "title": "PA",
                "clinic": "Noteworth General",
            },
        ]

        pd = ProviderDataParser(sample_data)
        pd.save_data_to_models()

        assert Employee.objects.count() == 2

        employee1 = Employee.objects.get(given_name="Jasper")
        assert employee1.title.name == "Dr."
        assert employee1.clinic.name == "Noteworth General"
