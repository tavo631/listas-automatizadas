

import re

def extraer_datos(texto):
    lineas = [l.strip() for l in texto.split("\n") if l.strip()]

    datos = {
        "nombre": "",
        "matricula": "",
        "carrera": "",
        "vigencia": ""
    }

    # -------- NOMBRE --------
    # Nombre suele estar en MAYÚSCULAS y en 1–2 líneas seguidas
    posibles_nombres = []
    for linea in lineas:
        if linea.isupper() and len(linea.split()) >= 2:
            posibles_nombres.append(linea)

    if len(posibles_nombres) >= 2:
        datos["nombre"] = posibles_nombres[0] + " " + posibles_nombres[1]
    elif len(posibles_nombres) == 1:
        datos["nombre"] = posibles_nombres[0]

    # -------- CARRERA --------
    # Buscar palabras clave de carrera
    carrera_keywords = ["ing.", "ingeniería", "desarrollo", "software", "gestión"]

    carrera_lineas = []
    for linea in lineas:
        if any(k.lower() in linea.lower() for k in carrera_keywords):
            carrera_lineas.append(linea)

    if carrera_lineas:
        datos["carrera"] = " ".join(carrera_lineas)



    # -------- VIGENCIA --------
    # Buscar año (ej: 2025, 2026)
    for linea in lineas:
        match = re.search(r"\b20\d{2}\b", linea)
        if match:
            datos["vigencia"] = match.group()
            break

    return datos
