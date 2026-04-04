from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from ocr import extract_numbers

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/scan', methods=['POST'])
def scan_image():
    file = request.files['image']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    numbers = extract_numbers(path)

    return jsonify({"numbers": numbers})

if __name__ == "__main__":
    app.run(debug=True)
