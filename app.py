from flask import Flask, render_template, request
import os
from ocr_core import run_ocr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    ocr_text = None
    image_url = None

    if request.method == 'POST':
        if 'image' not in request.files:
            ocr_text = "이미지 파일이 선택되지 않았습니다."
        else:
            file = request.files['image']
            if file.filename == '':
                ocr_text = "파일 이름이 비어 있습니다."
            else:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                ocr_text = run_ocr(filepath)
                image_url = filepath.replace("\\", "/")

    return render_template('index.html', image_url=image_url, ocr_text=ocr_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


