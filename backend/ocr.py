import easyocr
import cv2
import numpy as np
import re

reader = easyocr.Reader(['en'])

def _preprocess(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Upscale to help handwriting
    gray = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

    # Remove horizontal notebook lines
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    bw = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV, 31, 7
    )
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    detected_lines = cv2.morphologyEx(bw, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
    no_lines = cv2.subtract(bw, detected_lines)

    # Clean noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    no_lines = cv2.morphologyEx(no_lines, cv2.MORPH_CLOSE, kernel, iterations=1)

    return no_lines

def extract_numbers(image_path):
    img = _preprocess(image_path)

    results = reader.readtext(
        img,
        detail=1,
        paragraph=False,
        allowlist='0123456789',
        contrast_ths=0.05,
        adjust_contrast=0.9,
        width_ths=0.3
    )

    numbers = []

    for (_, text, _) in results:
        found = re.findall(r'\d+', text)
        numbers.extend(found)

    return numbers