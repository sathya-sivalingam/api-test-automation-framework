# =============================
# tests/conftest.py
# =============================
import pytest
from utils.config_loader import load_config
from clients.user_client import UserClient
from clients.auth_client import AuthClient

@pytest.fixture(scope="session")
def config():
    return load_config("dev")

@pytest.fixture(scope="session")
def auth_token(config):
    client = AuthClient(config['base_url'])
    return "dummy-token"  # Replace with real login

@pytest.fixture
def user_client(config):
    return UserClient(config['base_url'])
