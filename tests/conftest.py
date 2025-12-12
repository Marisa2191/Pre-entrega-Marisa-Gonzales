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
