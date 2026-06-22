import easyocr
import cv2
import re

reader = easyocr.Reader(['en'])

def extract_numbers(image_path):

    img = cv2.imread(image_path)

    results = reader.readtext(img)

    numbers = []

    for (_, text, _) in results:

        found = re.findall(r'\d+', text)

        numbers.extend(found)

    return numbers