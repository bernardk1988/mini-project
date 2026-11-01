
import pdfplumber
from pathlib import Path


def extract_textfrom_pdf(input_file):
    pages =[]
    with pdfplumber.open(input_file) as pdf:
        for page_number,page in enumerate(pdf.pages,start=1):
            text = page.extract_text() or ""
            pages.append({"page_number":page_number,"text":text})
            metadata = {
                "file_name":Path(input_file).name,
                "page_number":len(pdf.pages),
                "text_count":sum(len(page["text"]) for page in pages)
            }
        return pages,metadata
