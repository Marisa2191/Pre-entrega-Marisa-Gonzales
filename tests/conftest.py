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

