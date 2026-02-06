# ocr/lector_matricula.py

import cv2
import pytesseract
import re

def leer_matricula_desde_imagen(ruta_imagen):
    img = cv2.imread(ruta_imagen)
    h, w, _ = img.shape

    # 🔹 Recortar zona inferior (donde están los números del código)
    roi = img[int(h * 0.75):h, int(w * 0.2):int(w * 0.8)]


    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    # OCR SOLO números
    texto = pytesseract.image_to_string(
        gray,
        config="--psm 7 -c tessedit_char_whitelist=0123456789"
    )


    match = re.search(r"\d{6,10}", texto)
    if match:
        return match.group()

    return ""
