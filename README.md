# Calculadora de Matrices - Arquitectura Cliente-Servidor

Este proyecto es una calculadora interactiva que permite realizar operaciones de suma y multiplicación de matrices. Está diseñado para demostrar una arquitectura en la que un cliente web (Frontend) puede procesar datos localmente o comunicarse con distintos lenguajes en el servidor (Backend).

## Tecnologías Utilizadas

* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API).
* **Backend 1:** NodeJS con Express.
* **Backend 2:** Python con Flask.

---

## Requisitos Previos

Para ejecutar este proyecto de manera local, necesitás tener instalados:

* [Node.js y npm](https://nodejs.org/)
* [Python 3 y pip](https://www.python.org/)

---

## Configuración y Ejecución

El proyecto está dividido en tres partes. Para que la versión cliente-servidor funcione correctamente, debes levantar ambos backends.

### 1. Levantar el Backend en NodeJS (Puerto 3000)

1. Abre una terminal y navega hasta la carpeta donde guardaste el archivo `server.js`.
2. Inicializa el proyecto y descarga las dependencias:
 
   npm init -y
   npm install express cors

Ejecuta el servidor:

node server.js

