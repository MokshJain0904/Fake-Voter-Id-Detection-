import pytesseract
from PIL import Image

# EXPLICIT path (this is the key)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("Tesseract version:", pytesseract.get_tesseract_version())

img = Image.open("images/sample.jpg")
text = pytesseract.image_to_string(img)

print("OCR Output:\n", text)
