[![QA Automation CI](https://github.com/Marisa2191/Pre-entrega-Marisa-Gonzales/actions/workflows/ci.yml/badge.svg)](https://github.com/Marisa2191/Pre-entrega-Marisa-Gonzales/actions/workflows/ci.yml)

# 🧪 QA Automation – Selenium & Pytest

## 📌 Descripción del Proyecto

Este proyecto corresponde a una **Entrega de QA Automation**, donde se implementa un framework de automatización de pruebas utilizando **Selenium WebDriver** y **Pytest** en Python.

El objetivo principal es validar funcionalidades clave de la aplicación **SauceDemo**, aplicando buenas prácticas de automatización, manejo de fixtures, logging, reportes y control de versiones con GitHub.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.13**
* **Selenium WebDriver**
* **Pytest**
* **WebDriver Manager**
* **Pytest‑HTML** (reportes)
* **Logging (logging module)**
* **Git & GitHub**

---

## 📂 Estructura del Proyecto

```
Pre-entrega-Marisa-Gonzales/
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── tests_api/
│
├── utils/
│   └── logger.py
│
├── data/
│   └── login_data.csv
│
├── reports/
│   └── screenshots/
│
├── logs/
│   └── ejecucion.log
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Casos de Prueba Automatizados

### 🔹 Login

* Login exitoso con credenciales válidas
* Manejo de datos desde archivo CSV

### 🔹 Inventario

* Verificación de carga de productos

### 🔹 Carrito de Compras

* Agregar producto al carrito
* Verificación del badge del carrito
* Validación del producto agregado

---

## 📝 Logging

Se implementó un sistema de **logging centralizado** que registra:

* Inicio y fin de cada test
* Errores durante la ejecución
* Fallos de tests

Los logs se almacenan en:

```
logs/ejecucion.log
```

Esto permite una rápida depuración y trazabilidad de la ejecución.

---

## 📸 Evidencias en Fallos

Cuando un test falla:

* Se captura automáticamente un **screenshot**
* Se guarda en:

```
reports/screenshots/
```

* El evento queda registrado en el log

---

## ▶️ Ejecución de Pruebas

### 1️⃣ Activar entorno virtual

```bash
source .venv/bin/activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar todos los tests

```bash
pytest -v
```

### 4️⃣ Ejecutar un test específico

```bash
pytest tests/test_cart.py -v
```
---
## 🔄 Integración CI/CD

El proyecto cuenta con integración continua (CI) mediante **GitHub Actions**.

El pipeline se ejecuta automáticamente en los siguientes eventos:
- Push a la rama `main`
- Creación de Pull Requests sobre `main`

Durante la ejecución del workflow:
- Se instala el entorno de Python y las dependencias necesarias
- Se ejecutan todos los tests automatizados con Pytest
- Se genera un reporte HTML de Pytest
- El reporte se almacena como **artifact** de la ejecución
- En caso de fallos, se capturan screenshots automáticamente

El estado del pipeline se visualiza en tiempo real mediante el badge incluido en este README.

---
## 🗂 Control de Versiones

El proyecto se encuentra versionado utilizando **Git y GitHub**.

Durante el desarrollo:
- Se realizaron commits frecuentes y descriptivos para documentar el progreso del proyecto
- La rama principal (`main`) contiene la versión estable del sistema
- GitHub se utilizó como repositorio central para el control de versiones y la documentación

---
## 📊 Reportes

El proyecto utiliza **pytest-html** para la generación de reportes HTML detallados.

Los reportes incluyen:
- Listado de tests ejecutados
- Estado de cada test (pasado / fallado)
- Duración de ejecución
- Evidencias visuales (screenshots) en caso de fallos

En ejecuciones locales, los reportes se generan en el directorio `reports/`.

En ejecuciones CI/CD, los reportes se almacenan automáticamente como **artifacts en GitHub Actions**.


---

## 🚫 Archivos Ignorados

El archivo `.gitignore` excluye correctamente:

* Entornos virtuales
* Caché de Pytest y Python
* Logs y reportes
* Archivos del sistema operativo

---

## 👩‍💻 Autora

**Marisa Gonzales**
QA Analyst – Automation

---

## ✅ Estado del Proyecto

Proyecto finalizado con:
- Tests automatizados funcionales y de API
- Logging centralizado
- Reportes HTML
- Integración CI/CD activa
