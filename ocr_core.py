import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def run_ocr(image_path):
    text = pytesseract.image_to_string(image_path, lang="kor+eng")
    return text



