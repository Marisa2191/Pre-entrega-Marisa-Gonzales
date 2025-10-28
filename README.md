# 🧪 Pre-entrega – Marisa Gonzales

Este repositorio contiene los ejercicios de automatización de la Pre-entrega (Python + Selenium + Pytest).

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