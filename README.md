# 🧪 Pre-entrega – Marisa Gonzales

Este repositorio contiene los ejercicios de automatización de la Pre-entrega (Python + Selenium + Pytest).
## 🧩 Propósito del proyecto

Este proyecto corresponde a la **Pre-Entrega de Automatización QA**, utilizando **Python + Selenium + Pytest**.  
El objetivo es automatizar pruebas funcionales en el sitio [saucedemo.com](https://www.saucedemo.com) para validar:

- Login exitoso.
- Visualización del catálogo de productos.
- Interacción con el carrito de compras.

---

## 🧠 Tecnologías utilizadas

- **Python 3.13**
- **Selenium 4.21.0**
- **Pytest 8.2.1**
- **Pytest-HTML 4.1.1**
- **Webdriver-Manager 4.0.2**

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Marisa2191/Pre-entrega-Marisa-Gonzales.git
   cd Pre-entrega-Marisa-Gonzales
2. Crear y activar un entorno virtual:
    python3 -m venv .venv
    source .venv/bin/activate
3. Instalar las dependencias:
    pip install -r requirements.txt

▶️ Ejecución de pruebas

Para ejecutar todas las pruebas y generar el reporte HTML:
    pytest -v -s --html=reports/reporte.html --self-contained-html

📊 Reporte HTML

El reporte se genera automáticamente en:
    reports/reporte.html
Puede abrirse en el navegador con doble clic o desde VS Code con “Reveal in Finder”.

📸 Evidencias automáticas

Si se desea agregar capturas automáticas o logs en caso de fallo, pueden almacenarse en:
   reports/screenshots/
(Esta carpeta ya está creada en la estructura del proyecto.)

✅ Todos los tests finalizan con resultado “PASSED”.

---

## 🚀 Ejercicio 1: Login exitoso  
Automatiza el login en [https://www.saucedemo.com](https://www.saucedemo.com) validando el acceso correcto.

### Cómo ejecutar
```bash
pytest -v -k test_login_exitoso
```
---

## 🛒 Ejercicio 2: Catálogo de productos  
Valida que el título de la página de inventario sea correcto, verifica la presencia de productos y muestra el nombre y precio del primero.

### Cómo ejecutar
```bash
pytest -v -k test_catalogo_productos -s
```

## 📸 Resultado esperado
- ✅ El login redirige correctamente a `/inventory.html`.
- ✅ Se muestra el título **“Products”**.
- ✅ En el catálogo se lista al menos un producto.
- ✅ El primer producto visible es **“Sauce Labs Backpack - $29.99”**.

---
---

## 🧺 Ejercicio 3: Interacción con productos (Carrito de compras)

Valida que el usuario pueda añadir un producto al carrito, verificar que el contador se incremente correctamente y confirmar que el producto añadido aparezca en el carrito.

### Cómo ejecutar
```bash
pytest -v -k test_agregar_primer_producto_al_carrito -s
```
🧾 Resultado esperado

✅ El usuario puede hacer login correctamente.

✅ Se agrega el primer producto de la lista al carrito.

✅ El contador del carrito muestra "1" después de agregar el producto.

✅ Al ingresar al carrito, se visualiza el producto agregado: “Sauce Labs Backpack”.

---

