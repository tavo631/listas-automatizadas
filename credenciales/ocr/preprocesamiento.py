

import cv2
import os

def preprocesar_imagen(ruta_entrada, ruta_salida):
    """
    Preprocesa la imagen para mejorar la lectura OCR
    """
    if not os.path.exists(ruta_entrada):
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_entrada}")

    img = cv2.imread(ruta_entrada)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(ruta_salida, gray)

    return gray
