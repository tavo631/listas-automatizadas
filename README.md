# 📸 Sistema de Control de Asistencia mediante Lectura de Credenciales

**Versión:** v1.2  
**Estado:** Prototipo funcional  

Proyecto académico orientado a la automatización del registro de asistencia escolar mediante el uso de procesamiento digital de imágenes, reconocimiento óptico de caracteres (OCR) y una interfaz web básica.

---

## 👥 Equipo de Trabajo
- **José Gustavo López Gracia**
- **Poom Flores**

---

## 🧠 Descripción General

El sistema permite registrar la asistencia de los estudiantes a partir de una imagen capturada de la credencial escolar. A través de técnicas de preprocesamiento de imagen y OCR, se extrae información relevante como nombre, carrera y matrícula, generando registros automatizados de asistencia.

El proyecto tiene como finalidad reducir errores humanos, optimizar procesos administrativos y mejorar la transparencia en el control académico dentro de instituciones educativas.

---

## 🧩 Estado Actual del Proyecto (Versión)

La versión actual del sistema corresponde a la **v1.2**, la cual implementa la base funcional del control de asistencia mediante lectura de credenciales, incluyendo procesamiento de imágenes, OCR y generación de registros en formato CSV.

Esta versión se considera una **etapa intermedia del desarrollo**, identificándose las siguientes áreas de mejora:

- Integración más robusta entre el **frontend y el backend**, mediante servicios web (API REST).
- Comunicación en tiempo real entre la interfaz web y el sistema de procesamiento.
- Persistencia de datos mediante una base de datos relacional.
- Mejora en la precisión de lectura de la matrícula.

Como **línea de evolución del proyecto**, se plantea la incorporación de **reconocimiento facial** como mecanismo complementario o alternativo al uso de credenciales físicas, con el objetivo de incrementar la seguridad y automatizar completamente la validación de identidad.

---

## ⚙️ Tecnologías Utilizadas

- **Lenguaje:** Python  
- **Procesamiento de imágenes:** OpenCV  
- **OCR:** Tesseract OCR  
- **Frontend:** HTML5, CSS3  
- **Gestión de datos:** CSV (fase actual)  
- **Control de versiones:** Git / GitHub  

---

## ▶️ Cómo Ejecutar el Proyecto (Código Fuente)

### 1️⃣ Requisitos Previos
- Python 3.10 o superior  
- Git  
- Tesseract OCR instalado y agregado al PATH del sistema  

### 2️⃣ Clonar el repositorio
```bash
git clone https://github.com/tavo631/listas-automatizadas.git
cd listas-automatizadas
