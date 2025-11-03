import pytesseract
import platform

def run_ocr(image_path):
    # 리눅스 환경에서는 시스템 PATH에 설치됨
    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    text = pytesseract.image_to_string(image_path, lang="kor+eng")
    return text


