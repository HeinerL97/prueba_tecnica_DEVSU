# README – Automatización de Pruebas API y E2E

## 1. Descripción del proyecto

Este repositorio contiene dos proyectos de automatización:

### API Petstore

Automatización de pruebas para la API pública de Petstore, validando el ciclo completo **CRUD** del recurso **usuario**:

* **Create** → Crear usuario
* **Read** → Consultar usuario
* **Update** → Actualizar usuario
* **Delete** → Eliminar usuario

Las pruebas validan códigos de estado HTTP, integridad de datos y persistencia de cambios usando datos dinámicos.

### E2E Demoblaze

Automatización de pruebas de extremo a extremo para el sitio web **[Demoblaze](https://www.demoblaze.com/)**, validando el flujo completo de compra:

* Selección de productos
* Agregado al carrito
* Visualización del carrito
* Completar formulario de compra
* Confirmación de compra

Se utiliza **Page Object Model (POM)** para mantener un código organizado y fácil de mantener.

---

## 2. Herramientas utilizadas

### API Petstore

* Node.js
* Cypress
* Mochawesome (reportes)
* Documentación de API: [https://petstore.swagger.io/](https://petstore.swagger.io/)

### E2E Demoblaze

* Python 3.8+
* Selenium WebDriver
* Pytest
* Allure Reports

---

## 3. Conclusiones

* Este repositorio permite validar tanto la **API** como el **flujo web E2E**, asegurando calidad integral.
* El uso de **Cypress** y **Pytest + POM** facilita la mantenibilidad y escalabilidad del proyecto.
* Los reportes generados permiten analizar fallos, tiempos y pasos de cada prueba.
* Se recomienda ejecutar pruebas periódicamente y revisar los reportes para detectar regresiones.
