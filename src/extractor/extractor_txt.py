

#text

from pathlib import Path
import pdfplumber
import re

def extract_data12(file_path,file_format):
    path =Path(file_path)
    pages = []
    full_text = ""
    if file_format == "txt":
        full_text = path.read_text(encoding="utf-8",errors="ignore")
        pages.append({
            "page_number":1,
            "text":full_text
        }) 
    elif file_format == "pdf":
        with pdfplumber.open(path) as pdf:
            for number,page in enumerate(pdf.pages,start=1):
                text = page.extract_text() or ""
                pages.append({
                    "page_number":number,
                    "text":text,
                })
                full_text +=text + "\n"
    else:
        raise ValueError("unsupported format")
    
    keywords = ["invoice","student","total","email","date","contact"]
    found_keywords = {}
    for word in keywords:
        count = len(re.findall(
                rf"\b{word}\b",
                full_text,
                re.IGNORECASE,
        ))
        if count > 0:
           found_keywords[word] = count
    email = re.findall(
    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
    full_text
    )
    phone = re.findall(
    r"(?<!\d)[6-9]\d{9}(?!\d)",
    full_text
    )
    date = re.findall(
    r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",
    full_text
    )
    metadata = {
            "file_name":path.name,
            "file_type":path.suffix,
            "file_size":round(path.stat().st_size / 1024, 2),
            "page_count":len(pages),
            "word_count":len(full_text.split()),
            "character_count":len(full_text),
            "line_count":len(full_text.splitlines()),
        }
    extracted_fields = {
            "email":email,
            "phone":phone,
            "date":date,
        } 
    return {
            "metadata":metadata,
            "pages":pages,
            "keywords":found_keywords,
            "extracted_fields":extracted_fields,
        }

