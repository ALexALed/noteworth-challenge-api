import logging
from celery import shared_task

from providers import provider_integration


logger = logging.getLogger(__name__)


@shared_task
def load_data_from_provider():
    logger.info("Loading data from provider")
    df = provider_integration.ProviderDataFetcher()
    df.get_provider_data()

    if df.data:
        dp = provider_integration.ProviderDataParser(df.data)
        dp.save_data_to_models()
