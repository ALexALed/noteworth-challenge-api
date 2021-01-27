import responses

from django.test import TestCase

from providers.tasks import load_data_from_provider
from providers.models import Employee


class LoadDataTaskTestCase(TestCase):
    @responses.activate
    def test_load_data_task(self):
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

        responses.add(
            responses.GET,
            "http://noteworth_challenge_api:5000/auth",
            body="12345",
            status=200,
        )

        responses.add(
            responses.GET,
            "http://noteworth_challenge_api:5000/providers",
            json={"providers": sample_data},
            status=200,
        )

        load_data_from_provider()

        assert Employee.objects.count() == 2
