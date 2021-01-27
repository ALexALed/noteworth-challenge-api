import logging
import hashlib
import json

from providers import request_utils
from providers.serializers import EmployeeSerializer


logger = logging.getLogger(__name__)


class ProviderDataFetcher:

    BASE_PROVIDER_URL = "http://noteworth_challenge_api:5000/"
    AUTH_URL = "auth"
    PROVIDERS_URL = "providers"

    def __init__(
        self,
    ):
        self.auth_token = None
        self.requests_adapter = request_utils.get_requests_session_with_failures()
        self.data = None

    @staticmethod
    def hash_token(token):
        return hashlib.sha256(
            f"{token}/{ProviderDataFetcher.PROVIDERS_URL}".encode("utf-8")
        ).hexdigest()

    def get_auth_token(self):
        auth_url = (
            f"{ProviderDataFetcher.BASE_PROVIDER_URL}{ProviderDataFetcher.AUTH_URL}"
        )
        try:
            response = self.requests_adapter.get(auth_url)
            if response.ok:
                self.auth_token = self.hash_token(
                    response.headers.get("Super-Secure-Token")
                )
            else:
                logger.error("Error %s for request %s", response.status_code, auth_url)
        except request_utils.RETRIES_ERROR:
            logger.exception("Max count of attempts retries, for request %s", auth_url)

    def get_provider_data(self):

        provider_data_url = f"{ProviderDataFetcher.BASE_PROVIDER_URL}{ProviderDataFetcher.PROVIDERS_URL}"

        if not self.auth_token:
            self.get_auth_token()

        if self.auth_token:
            try:
                response = self.requests_adapter.get(
                    provider_data_url, headers={"X-Request-Checksum": self.auth_token}
                )
                if response.ok:
                    try:
                        self.data = response.json().get("providers", [])
                    except json.decoder.JSONDecodeError:
                        logger.exception(
                            "Invalid data for request %s", provider_data_url
                        )
                else:
                    logger.error(
                        "Error %s for request %s",
                        response.status_code,
                        provider_data_url,
                    )
            except request_utils.RETRIES_ERROR:
                logger.exception(
                    "Max count of attempts retries, for request %s", provider_data_url
                )


class ProviderDataParser:
    def __init__(self, data):
        self.data = data

    def save_data_to_models(self):
        for each_data in self.data:
            data_serialized = EmployeeSerializer(data=each_data)
            logger.info("data {}", each_data)
            if data_serialized.is_valid():
                data_serialized.save()
            else:
                logger.error("Invalid data for %s", each_data)
