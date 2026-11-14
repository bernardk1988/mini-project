
import pdfplumber
from pathlib import Path
import re


def extract_textfrom_pdf(file_path):
    file_path = Path(file_path)
    result = {
        "file_name":file_path.name,
        "file_type":"PDF",
        "metadata":{},
        "page_count":0,
        "pages":[],
        "tables":[],
        "images":[],
        "extracted_fields":{},
        "raw_text":"",
    }
    all_text = []
    with pdfplumber.open(file_path) as pdf:
        result["metadata"]=pdf.metadata or {}
        result["metadata"].update({
            "file_name": file_path.name,
            "file_type": "PDF",
            "file_size_bytes": file_path.stat().st_size,
        })

        result["page_count"]=len(pdf.pages)
        for page_number,page in enumerate(pdf.pages,start=1):
            text = page.extract_text() or ""
            all_text.append(text)
            page_tables = page.extract_tables() or []
            for table_number, table in enumerate(page_tables,start=1):
                result["tables"].append({
                    "page":page_number,
                    "table_number":table_number,
                    "data":table,
                })
            for image_number,img in enumerate(page.images,start=1):
                result["images"].append({"page":page_number,
                                         "image_number":image_number,
                                         "width":img.get("width"),
                                         "height":img.get("height"),
                                         "x0":img.get("x0"),
                                         "top":img.get("top"),
                                         "x1":img.get("x1"),
                                         "bottom":img.get("bottom")})
                result["pages"].append({"page_number":page_number,
                                        "width":page.width,
                                        "height":page.height,
                                        "text":text})
        result["raw_text"]="\n".join(all_text)
        text = result["raw_text"]
        patterns = {
        "invoice_number": r"(?i)invoice\s*(?:no|number|#)?\s*[:\-]?\s*([A-Z0-9\-]+)",
        "date": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        "time": r"\b\d{1,2}:\d{2}(?:\s*[APap][Mm])?\b",
        "email": r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
        "phone": r"\b(?:\+?\d{1,3}[- ]?)?\d{10}\b",
        "amount": r"(?i)(?:total|amount|grand total)\s*[:\-]?\s*(?:₹|Rs\.?|INR)?\s*[\d,]+(?:\.\d{2})?"
        }
        for field, pattern in patterns.items():
            matches = re.findall(pattern, text)
            result["extracted_fields"][field] = (
            matches[0] if matches else None
            )
        return result
