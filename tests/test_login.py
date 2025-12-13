


import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()



def test_login_desde_csv(driver, login_data):

    for fila in login_data:
        usuario = fila["usuario"]
        password = fila["password"]
        debe_funcionar = str(fila["debe_funcionar"]).strip().lower() == "true"

        driver.delete_all_cookies()  # para que cada fila arranque “limpia”

        login_page = LoginPage(driver)

        logger.info(f"Intentando login con usuario: {usuario}")
        login_page.abrir_pagina()
        login_page.login_completo(usuario, password)

        if debe_funcionar:
            assert "inventory" in driver.current_url
            logger.info("Login exitoso validado correctamente.")
        else:
            mensaje = login_page.obtener_error()
            assert "Epic sadface" in mensaje
            logger.info("Login fallido validado correctamente.")
