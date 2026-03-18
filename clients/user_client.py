# =============================
# clients/user_client.py
# =============================
from clients.base_client import BaseClient

class UserClient(BaseClient):
    def get_users(self, headers=None):
        return self.get("/users", headers=headers)

    def get_user(self, user_id, headers=None):
        return self.get(f"/users/{user_id}", headers=headers)
