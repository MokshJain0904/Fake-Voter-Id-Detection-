import cv2
import pytesseract
import re

# Set tesseract path (VERY IMPORTANT on Windows)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Improve OCR accuracy
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(gray)
    return text


def extract_epic_number(text):
    """
    EPIC format: 3 letters + 7 digits (e.g., ABC1234567)
    """
    pattern = r"\b[A-Z]{3}[0-9]{7}\b"
    match = re.search(pattern, text.replace(" ", "").upper())

    if match:
        return match.group()
    return None


def validate_epic(epic):
    if epic is None:
        return False
    return bool(re.match(r"^[A-Z]{3}[0-9]{7}$", epic))


def ocr_analysis(image_path):
    text = extract_text(image_path)
    epic = extract_epic_number(text)
    is_valid = validate_epic(epic)

    return {
        "ocr_text": text,
        "epic_number": epic,
        "epic_valid": is_valid
    }
