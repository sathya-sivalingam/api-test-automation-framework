# =============================
# utils/config_loader.py
# =============================
import yaml


def load_config(env="dev"):
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
    return config[env]
