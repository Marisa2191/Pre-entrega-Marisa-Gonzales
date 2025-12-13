from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def completar_datos(self, nombre, apellido, cp):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(nombre)
        self.driver.find_element(*self.LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(cp)
        return self

    def continuar(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
        return self
