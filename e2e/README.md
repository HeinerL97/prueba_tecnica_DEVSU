# README – Automatización de pruebas E2E Demoblaze

## 1. Descripción del proyecto

Este proyecto contiene la automatización de pruebas de extremo a extremo (E2E) para el sitio web Demoblaze.

Las pruebas automatizadas validan el flujo de compra completo en la tienda online.

El flujo incluye:

* Selección de dos productos
* Agregado al carrito
* Visualización del carrito
* Diligenciamiento del formulario de compra
* Confirmación de la compra

Se utilizó el patrón **Page Object Model (POM)** para mejorar la mantenibilidad del código y separar la lógica de las páginas del flujo de prueba.

## 2. Herramientas

* Python
* Selenium WebDriver
* Pytest
* Allure Reports (para generación de reportes)

Sitio web bajo prueba: https://www.demoblaze.com/

## 3. Prerrequisitos

Antes de ejecutar el proyecto es necesario tener instaladas las siguientes herramientas.

### 3.1 Instalar Python

Descargar Python (versión 3.8 o superior) desde el sitio oficial:
https://www.python.org/

### 3.2 Java y Allure (Opcional)

Para la visualización de reportes locales con Allure es necesario tener instalado Java y la herramienta de línea de comandos de Allure.

## 4. Instalación

### 4.1 Clonar el repositorio y acceder

Ejecutar en la terminal:

```shell
git clone <url-del-repositorio>
```

Entrar a la carpeta del proyecto:

```shell
cd e2e
```

### 4.2 Configuración del entorno

1. **Crear entorno virtual**
   Se recomienda crear un entorno virtual para aislar las dependencias.

   ```shell
   python -m venv venv
   ```

2. **Activar el entorno virtual**

   * Windows:
     ```shell
     venv\Scripts\activate
     ```
   * Linux/macOS:
     ```shell
     source venv/bin/activate
     ```

3. **Instalar dependencias**

   ```shell
   pip install -r requirements.txt
   ```

## 5. Estructura del proyecto

El proyecto sigue el patrón **Page Object Model (POM)**:

* **pages/**: Contiene las clases que representan las páginas web (Home, Cart, Product, etc.) y sus interacciones.
* **tests/**: Contiene los scripts de prueba que ejecutan los flujos utilizando las páginas.
* **conftest.py**: Configuración compartida de Pytest (fixtures del navegador).

## 6. Casos de prueba automatizados

El escenario principal valida el flujo de compra exitoso ("Happy Path"):

1. **Home Page**: Navegación y selección de categorías.
2. **Selección de Productos**: Se agregan dos productos distintos al carrito.
3. **Carrito de Compras**: Validación de productos agregados.
4. **Checkout**: Completar formulario con datos de prueba.
5. **Confirmación**: Validación del mensaje "Thank you for your purchase!".

## 7. Ejecutar las pruebas

### 7.1 Ejecución simple

Ejecuta todas las pruebas desde la terminal:

   ```shell
   pytest
   ```

### 7.2 Ejecución con generación de reportes

Ejecuta las pruebas y guarda los resultados para Allure:

   ```shell
   pytest --alluredir=allure-results
   ```

## 8. Generación de reportes

El proyecto utiliza **Allure Reports**.

Para visualizar el reporte HTML detallado después de la ejecución:

```shell
allure serve allure-results
```

Esto abrirá automáticamente una ventana en tu navegador con estadísticas, gráficos y el paso a paso de la ejecución.

