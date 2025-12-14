import os
import sys
import re
import csv
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# =========================
# PYTHONPATH (CLAVE)
# =========================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from utils.logger import get_logger

logger = get_logger()

# =========================
# FIXTURE DRIVER
# =========================
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    # Detectar CI (GitHub Actions setea CI=true)
    is_ci = os.getenv("CI", "false").lower() == "true"

    if is_ci:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)

    yield drv
    drv.quit()


# =========================
# LOGIN DATA CSV
# =========================
@pytest.fixture
def login_data():
    ruta = Path(ROOT_DIR) / "data" / "login_data.csv"
    data = []

    with ruta.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["debe_funcionar"] = row["debe_funcionar"].lower() == "true"
            data.append(row)

    return data

# =========================
# HELPERS
# =========================
def _safe_filename(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", text)

# =========================
# SCREENSHOT EN FALLA
# =========================
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return

        screenshots_dir = os.path.join(ROOT_DIR, "reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{ts}_{_safe_filename(item.name)}.png"
        filepath = os.path.join(screenshots_dir, filename)

        driver.save_screenshot(filepath)
        logger.error(f"Test fallido: {item.name} | Screenshot: {filepath}")

# =========================
# LOG INICIO / FIN
# =========================
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logger.info(f"INICIO TEST: {item.name}")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    logger.info(f"FIN TEST: {item.name}")
