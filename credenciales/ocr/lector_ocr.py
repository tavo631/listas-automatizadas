

import pytesseract
from utils.configuracion import RUTA_TESSERACT


pytesseract.pytesseract.tesseract_cmd = RUTA_TESSERACT

def leer_texto(imagen):
    """
    Lee el texto de una imagen usando OCR
    """
    texto = pytesseract.image_to_string(imagen, lang="spa")
    return texto



