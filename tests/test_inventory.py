from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_catalogo_productos(driver):
    # Login
    login = LoginPage(driver)
    login.abrir_pagina()
    login.login_completo("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(driver)
    inventory.esperar_cargue()

    assert inventory.obtener_titulo() == "Products"
    assert inventory.cantidad_productos() > 0

    nombre, precio = inventory.obtener_nombre_y_precio_primer_producto()
    print(f"Primer producto: {nombre} - {precio}")

    