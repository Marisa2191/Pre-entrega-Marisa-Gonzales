from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get(self.URL)

    def login_completo(self, usuario, password):
        self.driver.find_element(*self.USERNAME).send_keys(usuario)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_LOGIN).click()

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR_MSG).text

