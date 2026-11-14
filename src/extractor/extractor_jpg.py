
from pathlib import Path
from PIL import Image
import pytesseract
import pandas as pd
import re
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_jpg(image_path):
    image_path = Path(image_path) 
    with Image.open(image_path) as original:
        metadata = {
            "file_name":image_path.name,
            "format": original.format,
            "mode":original.mode,
            "width":original.width,
            "height":original.height,
            "size_bytes":image_path.stat().st_size,
        }
        image = original.convert("RGB")
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )
    processed = cv2.GaussianBlur(
        gray, (3, 3), 0
    )
    config = "--oem 3 --psm 6"
    raw_text = pytesseract.image_to_string(processed,lang="eng",config=config)
    bill_info = {}
    bill_match = re.search(
        r"(?:bill|invoice|receipt)\s*"
        r"(?:no\.?|number|#)?\s*[:\-]?\s*"
        r"([A-Z0-9][A-Z0-9/-]*)",
        raw_text,
        re.IGNORECASE
    )
    bill_info["bill_number"] = (bill_match.group(1) if bill_match else None)
     # Date
    date_match = re.search(
        r"\b(?:[A-Z][a-z]{2,8}\s+\d{1,2},\s*\d{4}|\d{1,2}[-/]\d{1,2}[-/]\d{4})\b",
        raw_text
    )
    bill_info["bill_date"] = (date_match.group(0) if date_match else None)
    # Time
    time_match = re.search(
        r"\b(?:[01]?\d|2[0-3]):[0-5]\d"
        r"(?::[0-5]\d)?\s*(?:AM|PM)?\b",
        raw_text,
        re.IGNORECASE
    )
    bill_info["bill_time"] = (time_match.group(0) if time_match else None)
    total_amount = None
    for line in raw_text.splitlines():
        if re.search(
            r"\b(grand\s*total|total\s*amount|"
            r"amount\s*payable|net\s*amount|total)\b",
            line,
            re.IGNORECASE
        ):
            amount_match = re.search(
                r"(?:₹|Rs\.?|INR)?\s*"
                r"\d[\d,]*(?:\.\d{1,2})?",
                line,
                re.IGNORECASE
            )
            if amount_match:
                total_amount = amount_match.group(0).strip()
                break
    bill_info["total_amount"] = total_amount
    return metadata,raw_text,bill_info