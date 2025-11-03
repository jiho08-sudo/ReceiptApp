import pytesseract
import platform

def run_ocr(image_path):
    system = platform.system()
    if system == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    else:
        pytesseract.pytesseract.tesseract_cmd = "tesseract"  # Render(Ubuntu) 기본 PATH 사용

    text = pytesseract.image_to_string(image_path, lang="kor+eng")
    return text


