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
