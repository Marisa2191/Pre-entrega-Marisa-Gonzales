from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso(driver):
    # 1) abrir la página
    driver.get("https://www.saucedemo.com/")

    # 2) completar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 3) clic en Login
    driver.find_element(By.ID, "login-button").click()

    # 4) validar: url correcta + título visible
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert "Products" in titulo.text
