from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_primer_producto_al_carrito(driver):
    wait = WebDriverWait(driver, 10)

    # 0) Ir a login
    driver.get("https://www.saucedemo.com/")

    # 1) Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2) Esperar inventory
    wait.until(EC.url_contains("inventory.html"))
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    # 3) Tomar primer producto y su nombre
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # 4) Click "Add to cart" del primer producto (botón correcto)
    boton_add = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    boton_add.click()

    # 5) Esperar que el badge sea "1" (evita cuelgues)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    # 6) Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.url_contains("cart.html"))

    # 7) Verificar producto en carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_carrito) == 1

    nombre_en_carrito = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre
