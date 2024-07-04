import pyautogui
from PIL import Image
from pytesseract import *

try:
    from config import TESSERACT_PATH
except ImportError:
    TESSERACT_PATH = None
    
pytesseract.tesseract_cmd = TESSERACT_PATH

img_name = "text2"
img = Image.open(f"Images/{img_name}.png")

output = pytesseract.image_to_string(img)

print(output)