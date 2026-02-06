import sys
import os
import pandas as pd


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


from ocr.preprocesamiento import preprocesar_imagen
from ocr.lector_ocr import leer_texto
from ocr.extractor_datos import extraer_datos
from ocr.lector_matricula import leer_matricula_desde_imagen

# ------------------ RUTAS ------------------
RUTA_IMAGEN = "data/imagenes/aguero.jpg"
RUTA_IMAGEN_PROCESADA = "data/imagenes/procesada.jpg"
RUTA_RESULTADO = "data/resultados/credenciales.csv"


def main():
    print("📸 Iniciando lectura de credencial...")

    # 1. Preprocesar imagen
    print("🛠 Preprocesando imagen...")
    imagen = preprocesar_imagen(RUTA_IMAGEN, RUTA_IMAGEN_PROCESADA)

    # 2. Leer texto con OCR
    print("🔍 Leyendo texto con OCR...")
    texto = leer_texto(imagen)

    print("\n📄 TEXTO DETECTADO:\n")
    print(texto)

    # 3. Extraer datos por OCR (nombre, carrera, etc.)
    print("\n🧠 Extrayendo datos por OCR...")
    datos = extraer_datos(texto)

    # 4. Leer matrícula desde los NÚMEROS del código de barras
    print("📊 Leyendo matrícula desde números impresos...")
    matricula = leer_matricula_desde_imagen(RUTA_IMAGEN)

    if matricula:
        datos["matricula"] = matricula
    else:
        datos["matricula"] = ""

    # 5. Mostrar resultados
    print("\n✅ DATOS EXTRAÍDOS:")
    for clave, valor in datos.items():
        print(f"{clave.capitalize()}: {valor}")

    # 6. Guardar resultados
    print("\n💾 Guardando resultados...")
    os.makedirs(os.path.dirname(RUTA_RESULTADO), exist_ok=True)

    df = pd.DataFrame([datos])
    df.to_csv(RUTA_RESULTADO, index=False)

    print(f"📁 Datos guardados en: {RUTA_RESULTADO}")
    print("\n🎉 Proceso finalizado correctamente.")


# ------------------ EJECUCIÓN ------------------
if __name__ == "__main__":
    main()
