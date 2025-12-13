from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def esperar_cargue(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return self

    def obtener_titulo(self):
        return self.driver.find_element(*self.TITLE).text

    def cantidad_productos(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def agregar_primer_producto_al_carrito(self):
        # botón del primer item
        primer_item = self.driver.find_elements(*self.INVENTORY_ITEMS)[0]
        btn = primer_item.find_element(By.TAG_NAME, "button")
        btn.click()
        return self

    def abrir_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()
        return self
    def obtener_nombre_y_precio_primer_producto(self):
         primer_item = self.driver.find_elements(*self.INVENTORY_ITEMS)[0]
         nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
         precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text
         return nombre, precio

