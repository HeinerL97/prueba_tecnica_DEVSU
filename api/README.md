# README – Automatización de pruebas API Petstore

## 1. Descripción del proyecto

Este proyecto contiene la automatización de pruebas para la API pública de Petstore.

Las pruebas automatizadas validan el ciclo completo **CRUD** del recurso  **usuario** .

CRUD significa:

* **Create** → Crear usuario
* **Read** → Consultar usuario
* **Update** → Actualizar usuario
* **Delete** → Eliminar usuario

Las pruebas validan códigos de estado HTTP, la integridad de los datos y la persistencia de los cambios, utilizando usuarios con datos dinámicos para evitar conflictos entre ejecuciones.

## 2. Herramientas

* Node.js
* Cypress
* Mochawesome (para generación de reportes)

Documentación de la API utilizada: [https://petstore.swagger.io/](https://petstore.swagger.io/)

# 3. Prerrequisitos

Antes de ejecutar el proyecto es necesario tener instaladas las siguientes herramientas.

## 2.1 Instalar Node.js

Descargar Node.js desde el sitio oficial:

[https://nodejs.org/](https://nodejs.org/)

Instalar la versión  **LTS (recomendada)** .

Una vez instalado, verificar en consola:

```shell
node -v
```

Debe mostrar algo similar a:

```
v20.x.x
```

Luego verificar npm:

```shell
npm -v
```

# 4. Instalación

Existen dos formas.

## Opción 1 – Descargar ZIP

1. Descargar el proyecto.
2. Descomprimirlo.
3. Abrir la carpeta del proyecto.

## Opción 2 – Clonar desde GitHub

Ejecutar en la terminal:

```shell
git clone <url-del-repositorio>
```

Entrar a la carpeta del proyecto:

```shell
cd api
```

## 4.1 Instalar dependencias

Una vez dentro de la carpeta del proyecto ejecutar:

```shell
npm install
```

Este comando instalará todas las librerías necesarias para ejecutar las pruebas.

Entre ellas:

* Cypress
* Mochawesome
* Dependencias internas del proyecto

# 5. Estructura del proyecto

```
api/
├── cypress/
│   ├── e2e/
│   │   └── petstore/
│   │       └── user.cy.js
│   └── support/
│       └── e2e.js
├── reports/
├── cypress.config.js
├── package.json
└── readme.md
```

Descripción:

| Carpeta     | Descripción                                    |
| ----------- | ----------------------------------------------- |
| cypress/e2e | Contiene los casos de prueba                    |
| support     | Archivos de soporte de Cypress                  |
| reports     | Reportes generados después de ejecutar pruebas |

# 6. Casos de prueba automatizados

Las pruebas implementadas son:

### 1. Crear usuario

Se envía una solicitud **POST** para crear un nuevo usuario en el sistema.

Endpoint:

```
POST /user
```

### 2. Buscar usuario creado

Se valida que el usuario creado exista en el sistema.

Endpoint:

```
GET /user/{username}
```

### 3. Actualizar nombre y correo

Se actualizan los datos del usuario.

Endpoint:

```
PUT /user/{username}
```

### 4. Buscar usuario actualizado

Se valida que los cambios se hayan aplicado correctamente.

Endpoint:

```
GET /user/{username}
```

### 5. Eliminar usuario

Se elimina el usuario creado durante la prueba.

Endpoint:

```
DELETE /user/{username}
```

# 7. Ejecutar las pruebas

Existen dos formas de ejecutar las pruebas.

## 7.1 Ejecutar en modo automático

Este modo ejecuta todas las pruebas desde la terminal.

Ejecutar:

```shell
npm run cypress:run
```

La consola mostrará la ejecución de cada prueba.

Ejemplo:

```
✓ Crear usuario
✓ Buscar usuario creado
✓ Actualizar usuario
✓ Buscar usuario actualizado
✓ Eliminar usuario
```

## 7.2 Ejecutar en modo visual (interfaz gráfica)

Este modo abre la interfaz de Cypress.

Ejecutar:

```shell
npm run cypress:open
```

Luego:

1. Seleccionar **E2E Testing**
2. Seleccionar el navegador
3. Ejecutar el archivo de pruebas

```
user.cy.js
```

# 8. Generación de reportes

El proyecto genera reportes automáticos utilizando  **Mochawesome** .

Después de ejecutar las pruebas se generará la carpeta:

```
reports
```

Dentro encontrarás archivos como:

```
mochawesome.html
mochawesome.json
```

Para visualizar el reporte:

Abrir el archivo:

```
reports/mochawesome.html
```

Este archivo muestra:

* resultados de las pruebas
* tiempos de ejecución
* casos exitosos o fallidos

# 9. Flujo Recomendado

Para generar los reportes ejecutar:

```shell
npm run cypress:run
```

Luego abrir:

```
reports/mochawesome.html
```
