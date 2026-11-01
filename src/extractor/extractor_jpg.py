

import re
from pathlib import Path
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_image_metadata(image,file_name):
    return{
        "file_name":file_name,
        "format":str(image.format or "PDF page"),
        "mode":image.mode,
        "width":image.width,
        "height":image.height,
        "size_bytes":Path(file_name).stat().st_size 
        if Path(file_name).is_file() else 0
    }

def extract_data(file_path):
    file_path = Path(file_path)
    metadata = {"file_name":file_path.name}
    text=""
    if file_path.suffix.lower() == ".pdf":
        pages=convert_from_path(file_path, dpi=200)
        metadata["page_count"]= len(pages)
        metadata["file_type"]="PDF"
        for number,page in enumerate(pages,start=1):
            metadata["page_{number}_width"]=page.width
            metadata["page_{number}_height"]=page.height
            text+=f"----{number}----"
            text+=pytesseract.image_to_string(page)
        return metadata.pages
    else:
        with Image.open(file_path) as image:
            metadata.update(
                get_image_metadata(image,str(file_path))
            )
            text = pytesseract.image_to_string(image)
        metadata["file_type"]="Image"

    # Regex patterns for common invoice fields
    patterns = {
        "Invoice No": r"Invoice\s*(?:Number|No\.?)\s*[:#-]?\s*([A-Z0-9/-]+)",
        "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "Contact No": r"(?:Contact|Phone|Mobile)\s*(?:No\.?)?\s*[:#-]?\s*([+()\d][\d\s()+-]{7,}\d)",
        "Amount (Rs)": r"\bRs\.?\s*([0-9,]+(?:\.\d{1,2})?)",
        "Date": r"\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b",
        "Place": r"\bPlace\s*:\s*([^\n,]+)"
    }

    extracted = {}

    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        extracted[field] = match.group(1).strip() if match and match.lastindex else (
            match.group(0).strip() if match else "Not found"
        )

    return metadata, text, extracted