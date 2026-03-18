# =============================
# tests/test_users.py
# =============================
import pytest

@pytest.mark.smoke
def test_get_users(user_client):
    response = user_client.get_users()
    assert response.status_code == 200

@pytest.mark.regression
def test_get_single_user(user_client):
    response = user_client.get_user(1)
    assert response.status_code == 200
