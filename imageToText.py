import os
from PIL import Image
from pytesseract import *

try:
    from config import TESSERACT_PATH
except ImportError:
    TESSERACT_PATH = None

if TESSERACT_PATH:
    pytesseract.tesseract_cmd = TESSERACT_PATH

images_folder = "Images"
text_folder = "Text"

os.makedirs(text_folder, exist_ok = True)

for img_name in os.listdir(images_folder):
    if img_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(images_folder, img_name)
        img = Image.open(img_path)
        
        output = pytesseract.image_to_string(img)
        
        text_file_name = os.path.splitext(img_name)[0] + ".txt"
        text_file_path = os.path.join(text_folder, text_file_name)
        
        with open(text_file_path, "w", encoding = "utf-8") as text_file:
            text_file.write(output)
        
        print(f"Processed {img_name} to {text_file_name}")