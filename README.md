# 📷 Smart Vision Calculator

A web-based AI-powered calculator that extracts numbers from images using Optical Character Recognition (OCR) and performs mathematical calculations without manual typing.

## 🚀 Project Overview

Traditional calculators require users to manually enter numbers before performing calculations. This project eliminates manual data entry by allowing users to upload an image containing numbers, automatically detecting the numbers using OCR, and performing calculations on the selected values.

The project combines:

- Computer Vision
- Optical Character Recognition (OCR)
- Web Development
- Mathematical Expression Evaluation

## 🎯 Problem Statement

Shopkeepers, merchants, students, accountants, and general users often spend time manually entering numbers from bills, receipts, handwritten notes, and lists into calculators.

This project aims to:

- Extract numbers directly from images
- Reduce manual input errors
- Improve calculation speed
- Provide a user-friendly smart calculator experience

---

## ✨ Features

### Current Features

- Image Upload
- OCR-Based Number Detection
- Automatic Number Extraction
- Interactive Number Selection
- Addition Operation
- Web-Based Interface
- JSON API Backend

### Planned Features

- Subtraction
- Multiplication
- Division
- Multiple Sequential Operations
- Handwritten Text Recognition
- Real-Time Camera Scanning
- Mobile-Friendly Interface
- Calculation History
- Export Results
- Smart Bill Analysis
- Currency Detection
- AI-Based Error Correction

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Upload Image
  │
  ▼
Frontend (HTML/CSS/JavaScript)
  │
  ▼
Flask Backend API
  │
  ▼
OCR Engine
  │
  ▼
Number Extraction
  │
  ▼
Calculator Logic
  │
  ▼
Result Display
```

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask
- Flask-CORS

### Computer Vision & OCR

- OpenCV
- EasyOCR

### Data Processing

- NumPy
- Regular Expressions (Regex)

---

## 📂 Project Structure

```text
smart_calculator/
│
├── backend/
│   ├── app.py
│   ├── ocr.py
│   ├── frontend.html
│   ├── test.html
│   ├── uploads/
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/smart-vision-calculator.git
```

```bash
cd smart-vision-calculator/backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask
pip install flask-cors
pip install opencv-python
pip install easyocr
pip install numpy
```

---

## ▶️ Run Project

Start Backend Server:

```bash
python app.py
```

Server runs at:

```text
http://127.0.0.1:5000
```

Open:

```text
frontend.html
```

in your browser.

---

## 📸 How It Works

1. Upload an image containing numbers.
2. OCR extracts text from the image.
3. Numbers are detected and displayed.
4. User selects required numbers.
5. Calculator performs operations.
6. Result is displayed instantly.

---

## ⚠️ Current Limitations

- Handwritten text accuracy is limited.
- Complex handwriting styles may not be detected correctly.
- Multiple operations are under development.
- Real-time camera scanning is not yet implemented.

---

## 🔮 Future Enhancements

- PaddleOCR Integration
- Transformer-Based OCR Models
- Real-Time Webcam OCR
- Handwriting Recognition System
- AI-Based Number Validation
- Mobile Application
- Cloud Deployment
- Multi-Language OCR Support

---

## 📊 Learning Outcomes

Through this project, the following concepts were explored:

- Computer Vision
- OCR Systems
- REST APIs
- Flask Backend Development
- Frontend-Backend Communication
- Image Processing
- Mathematical Expression Evaluation

---

## 👨‍💻 Author

**Harsha Valaboju**

B.Tech CSE (AIML)  
SR University

GitHub: https://github.com/yourusername

---

## 📜 License

This project is developed for educational and research purposes.
