# 📄 Sistema de Registro Digital de Martillos Demoledores

## 📌 Resumen

**DEMOLICIONES CACEDA MENDOZA S.A.C.**, empresa dedicada al giro de preparación de terreno, gestiona actualmente el registro de uso de sus martillos demoledores de manera manual mediante formatos físicos. Para modernizar este proceso y facilitar su administración, se ha desarrollado un programa en **Python 3.12** que permite registrar, validar y almacenar digitalmente esta información, mejorando la eficiencia y reduciendo errores.

---

## 🏢 Datos de la Empresa

- **Razón social:** DEMOLICIONES CACEDA MENDOZA S.A.C.
- **Giro:** Preparación de terreno
- **Misión:** Ser la empresa más confiable en demolición, excavación y construcción, reconocida por su excelente asesoría profesional.
- **Visión:** Brindar un servicio de calidad, seguro y sostenible, logrando 0 accidentes y satisfacción del cliente.

---

## ⚙️ Situación Actual

Actualmente, se utiliza un formulario físico para registrar diariamente las actividades con los martillos demoledores. Este proceso presenta problemas como:

- Ineficiencia y consumo de tiempo.
- Errores de transcripción.
- Demoras en la obtención de reportes.
- Pérdida de información.
- Dificultad para el análisis de datos.
- Impacto ambiental por uso de papel.

---

## 💡 Propuesta de Innovación

Implementación de un **sistema digitalizado** mediante una aplicación en Python que permita:

- Registrar digitalmente tareas, horas y observaciones.
- Almacenar información en una base de datos estructurada.
- Generar reportes automatizados.
- Optimizar la gestión de recursos.

### 📲 Detalle del Nuevo Proceso:

**Entradas:**
- Fecha, hora de inicio y fin.
- Descripción de actividad.
- Proyecto asociado.

**Proceso:**
- Inicio de sesión.
- Registro y seguimiento de actividades.
- Almacenamiento seguro.
- Validación opcional.

**Salidas:**
- Datos en tiempo real.
- Reportes personalizables.
- Paneles de control.
- Información útil para nómina.

---

## 🛠️ Herramientas Utilizadas

- **Lenguaje:** Python 3.12
- **Base de datos:** Por definir (ej. CSV, SQLite)
- **Gestión de proyecto:** Trello (Product Backlog y Sprints)

---

## 📑 Algoritmo Propuesto (Pseudocódigo)

```plaintext
FUNCIÓN main()
    Mostrar encabezado
    Solicitar datos de equipo, fecha, operador, combustible
    Llamar a función registrar_parte_diario()
FIN FUNCIÓN
```

## 🖥️ Instalación y Ejecución 📦

### 📋 Requisitos

- Python **3.12** o superior instalado en tu equipo.
- Editor de texto o IDE (recomendado: VS Code, PyCharm).
- Opcional: Entorno virtual para aislar dependencias.

### 📥 Instalación

1. **Clona este repositorio**

```bash
git clone git@github.com:wistox07/programacion_trabajo_final.git
programacion_trabajo_final
```

## 🚀 Cómo ejecutar el proyecto

Sigue estos pasos para correr la aplicación desde tu terminal:

1. Abre tu terminal o consola de comandos.
2. Navega hasta la carpeta del proyecto:

```bash
cd ruta/del/proyecto
python trabajo_final.py
```

