import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
from PIL import Image

def run_ocr(image_path):
    """한글 + 영어 OCR"""
    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang='kor+eng', config='--oem 3 --psm 6')
        return text.strip()
    except Exception as e:
        print("OCR Error:", e)
        return "OCR 처리 중 오류가 발생했습니다."


