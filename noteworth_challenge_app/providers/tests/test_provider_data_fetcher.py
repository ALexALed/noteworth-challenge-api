import responses

from django.test import TestCase

from providers.provider_integration import ProviderDataFetcher


class ProviderDataFetcherTestCase(TestCase):
    @responses.activate
    def test_auth_method(self):
        responses.add(
            responses.GET,
            "http://noteworth_challenge_api:5000/auth",
            body="12345",
            status=200,
        )
        pf = ProviderDataFetcher()
        pf.get_auth_token()
        assert (
            pf.auth_token
            == "8d00fed28ed70600ca52dd263804975485b9c51ddeafd3dafdac6eefbd0d378a"
        )

    @responses.activate
    def test_providers_method(self):

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
        pf = ProviderDataFetcher()
        pf.get_provider_data()

        self.assertListEqual(pf.data, sample_data)
