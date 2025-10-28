from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_primer_producto_al_carrito(driver):
    # 1) Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2) Esperar a que cargue la página de inventario
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    # Tomar el PRIMER producto de la lista
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Guardar el nombre del producto (para validarlo en el carrito)
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # 3) Clic en "Add to cart" del primer producto
    boton_agregar = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    boton_agregar.click()

    # 4) Verificar que el contador del carrito marque "1"
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"

    # 5) Ir al carrito
    driver.find_element(By.ID, "shopping_cart_container").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    # 6) Verificar que el producto agregado esté en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_carrito) == 1

    nombre_en_carrito = items_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre_en_carrito == nombre

    print(f"✅ Producto agregado y verificado en carrito: {nombre}")
    
