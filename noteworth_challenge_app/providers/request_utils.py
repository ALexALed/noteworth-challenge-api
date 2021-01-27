import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


RETRIES_ERROR = requests.exceptions.RetryError


def get_requests_session_with_failures(max_retries=2):
    retry_strategy = Retry(
        total=max_retries,
        status_forcelist=[408, 429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    return http
