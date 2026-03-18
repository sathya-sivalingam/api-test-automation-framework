# =============================
# clients/auth_client.py
# =============================
from clients.base_client import BaseClient

class AuthClient(BaseClient):
    def login(self, username, password):
        response = self.post("/auth/login", {"username": username, "password": password})
        return response.json().get("token")
