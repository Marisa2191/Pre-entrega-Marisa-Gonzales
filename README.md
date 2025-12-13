# Proyecto Final – Automatización QA 🚀

Entrega final del **Proyecto de Automatización QA**, desarrollado con **Python + Selenium + Pytest**, aplicando buenas prácticas de testing automatizado.

---

## 📌 Objetivo del proyecto

Este proyecto tiene como objetivo demostrar la automatización de pruebas funcionales
sobre un sitio web demo, utilizando buenas prácticas como:

* Page Object Model (POM)
* Separación entre lógica de pruebas y lógica de interacción con la UI
* Data-driven testing
* Generación de evidencias automáticas ante fallos

El sitio utilizado para las pruebas es:
🔗 [https://www.saucedemo.com](https://www.saucedemo.com)

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Selenium WebDriver
* Pytest
* Pytest-HTML
* WebDriver Manager
* CSV (datos de prueba)

---

## 📂 Estructura del proyecto

```text
pages/          → Page Objects (interacción con la UI)
tests/          → Casos de prueba
utils/          → Utilidades (logger)
data/           → Datos de prueba (CSV)
reports/        → Reporte HTML y screenshots
```

---

## 🧩 Page Object Model (POM)

El proyecto implementa el patrón **Page Object Model**, separando claramente:

* La lógica de los tests
* De la lógica de interacción con la interfaz de usuario

Cada página del sistema cuenta con su propia clase dentro del directorio `pages/`:

* LoginPage
* InventoryPage
* CartPage
* CheckoutPage

Los tests interactúan únicamente con métodos de estas clases, logrando:

* Tests más legibles
* Código mantenible
* Reutilización de lógica

---

## 🔁 Data-driven testing

El login se ejecuta utilizando datos externos desde un archivo **CSV**, permitiendo probar
múltiples escenarios (válidos e inválidos) sin modificar el código del test.

---

## 📸 Evidencias automáticas (Screenshots)

Cuando una prueba falla, el sistema captura automáticamente una **screenshot** del navegador.

Las capturas se almacenan en:

```text
reports/screenshots/
```

El nombre del archivo incluye:

* Fecha y hora
* Nombre del test que falló

Esto facilita el análisis y la documentación de errores.

---

## ▶️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Marisa2191/Pre-entrega-Marisa-Gonzales.git
cd Pre-entrega-Marisa-Gonzales
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de pruebas

Ejecutar todos los tests:

```bash
pytest -v
```

Generar reporte HTML:

```bash
pytest --html=reports/reporte.html --self-contained-html
```

El reporte se genera en:

```text
reports/reporte.html
```

---

## 🧪 Casos de prueba implementados

* Login exitoso y fallido
* Validación del catálogo de productos
* Obtención de nombre y precio de productos
* Interacción con el carrito de compras


---

## 🌐 Pruebas de API (Requests)

Además de las pruebas UI con Selenium, el proyecto incluye pruebas de API utilizando la librería **requests**, validando:

- Códigos de estado HTTP
- Estructura de respuestas JSON
- Escenarios de éxito y error
- Encadenamiento de peticiones (POST → GET)

### 📁 Ubicación
Los tests de API están en la carpeta:

tests_api/

### ✅ Casos implementados (API pública: JSONPlaceholder)

**1) GET /posts (éxito)**
- Verifica `status_code == 200`
- Valida que la respuesta sea una lista y que tenga elementos

Archivo:
- `tests_api/test_api_jsonplaceholder.py`

**2) POST /posts (éxito)**
- Verifica `status_code in (200, 201)`
- Valida que la respuesta sea JSON (dict)
- Verifica que devuelva un `id` y que refleje campos enviados (title/body/userId)

Archivo:
- `tests_api/test_api_post_posts.py`

**3) POST /posts (error en endpoint)**
- Envía la petición a un endpoint inválido
- Verifica que el status sea de error (ej: 404)

Archivo:
- `tests_api/test_api_post_posts.py`

**4) DELETE /posts/{id}**
- Verifica un status esperado de borrado (ej: 200 o 204)
- Tolera respuesta vacía o `{}` (según comportamiento del servicio)

Archivo:
- `tests_api/test_api_delete_posts.py`

### 🔗 Encadenamiento de peticiones (Opcional)
Se implementa un flujo donde una petición depende de otra:

1. Se crea un recurso con **POST**
2. Se usa el `id` devuelto para intentar obtenerlo con **GET**

> Nota: JSONPlaceholder es un servicio “fake”, por lo que puede devolver un `id` creado pero no persistirlo realmente.
> Por eso el test valida el `id` del POST y maneja la respuesta del GET de forma esperable.

Archivo:
- `tests_api/test_api_chain_post_get.py`

### ▶️ Cómo ejecutar (API)

Ejecutar solo API:
```bash
pytest tests_api -v

Ejecutar solo encadenamiento POST → GET:

pytest tests_api/test_api_chain_post_get.py -v

Ejecutar todo el proyecto (UI + API):

pytest -v
---
## 📊 Estado del proyecto

✔️ Login automatizado
✔️ Catálogo de productos
✔️ Interacción con carrito
✔️ Page Object Model
✔️ Data-driven testing
✔️ Evidencias automáticas

🏁 **Proyecto finalizado y listo para su evaluación.**

---

## 👩‍💻 Autora

**Marisa Gonzales**
QA Analyst – Automation Testing
