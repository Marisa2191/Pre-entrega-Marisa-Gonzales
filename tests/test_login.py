


import pytest
from pages.login_page import LoginPage
from utils.logger import logger




@pytest.mark.parametrize(
    "usuario,password,debe_funcionar",
    [
        ("standard_user", "secret_sauce", True),   # Login válido
        ("admin", "1234", False),                  # Login inválido
    ],
)
def test_login_basico(driver, usuario, password, debe_funcionar):


    """
    Primer ejercicio del TP:
    - Login exitoso
    - Login fallido
    - Uso de Page Object Model
    """

    
    login_page = LoginPage(driver)


    logger.info(f"Intentando login con usuario: {usuario}")
    login_page.abrir_pagina()
    login_page.login_completo(usuario, password)

    if debe_funcionar:
        # Validamos que nos lleva al inventario
        assert "inventory" in driver.current_url
        logger.info("Login exitoso validado correctamente.")
    else:
        # Validamos mensaje de error
        mensaje = login_page.obtener_error()
        assert "Epic sadface" in mensaje
        logger.info("Login fallido validado correctamente.")
