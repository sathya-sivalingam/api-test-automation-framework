# =============================
# clients/base_client.py
# =============================
import requests
from utils.logger import get_logger

logger = get_logger()

class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        return requests.get(url, headers=headers)

    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        return requests.post(url, json=data, headers=headers)
