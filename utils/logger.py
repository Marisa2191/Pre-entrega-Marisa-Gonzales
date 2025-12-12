import logging
import os

def get_logger(name="framework"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # evita duplicar handlers

    logger.setLevel(logging.INFO)

    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler("logs/ejecucion.log", encoding="utf-8")
    console_handler = logging.StreamHandler()

    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(fmt)
    console_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

logger = get_logger()
