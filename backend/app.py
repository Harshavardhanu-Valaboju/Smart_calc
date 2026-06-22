from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import extract_numbers
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/scan", methods=["POST"])
def scan():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(filepath)

    numbers = extract_numbers(filepath)

    print("Detected Numbers:", numbers)

    return jsonify({
        "numbers": numbers
    })

if __name__ == "__main__":
    app.run(debug=True)