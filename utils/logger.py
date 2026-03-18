# =============================
# utils/logger.py
# =============================
import logging


def get_logger():
    logger = logging.getLogger("framework_logger")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
