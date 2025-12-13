import os
import sys

# Agrego la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


# Agrego la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()

import csv
from pathlib import Path
import pytest

@pytest.fixture
def login_data():
    ruta = Path(__file__).resolve().parents[1] / "data" / "login_data.csv"
    data = []

    with ruta.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["debe_funcionar"] = row["debe_funcionar"].lower() == "true"
            data.append(row)

    return data

# tests/conftest.py
import os
import re
from datetime import datetime
import pytest

def _safe_filename(text: str) -> str:
    # deja solo letras/números/guion/underscore
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", text)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Si el test falla en la fase 'call', toma screenshot usando el fixture 'driver'
    y lo guarda en reports/screenshots/
    """
    outcome = yield
    report = outcome.get_result()

    # Solo si falló el test (fase de ejecución real)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver is None:
            return  # no hay webdriver en este test

        # carpeta destino
        screenshots_dir = os.path.join(item.config.rootpath, "reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # nombre: fecha_hora + nombre_del_test
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = _safe_filename(item.name)
        filename = f"{ts}_{test_name}.png"
        filepath = os.path.join(screenshots_dir, filename)

        # sacar screenshot
        driver.save_screenshot(filepath)

        # opcional: mostrar ruta en consola
        print(f"\n📸 Screenshot guardado: {filepath}")


