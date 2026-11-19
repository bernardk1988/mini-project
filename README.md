# DocuMind – Multi-Format Processing Engine
![Python Logo](data/my.jpg)

## Overview

DocuMind is a Python-based document processing tool that automates file extraction, data cleaning, analysis, and conversion. 
It allows users to process different file formats such us 
- **PDF**
- **TXT**
- **XLSX**
- **JPG**  
from the command line and export the processed results into CSV or JSON files.

## Key Features

- PDF Processing: Extracts text, tables, images metadata, pdf metadata, and Extract important Fields using regular expression from PDF documents.

- Excel Processing: Reads XLSX files, handles missing values, and calculates summary statistics using Pandas.

- Text Processing: Text Metadata, Extracts important text fields using regular expression, identifies target keywords, and provides document information.

- Image Processing: Uses OCR(optical character recognizer) to extract text from images, Image metadata, Extract important text using regular expression.

- Data Analysis: Calculates row counts, column count, sums, averages, and other relevant statistics for structured data.

- Data Conversion: Converts extracted and processed data into CSV or JSON formats.

- Terminal Display: Displays extracted data and processing summaries in a readable table format.

- File Management: Automatically locates input files and saves output files in the appropriate directories.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Argparse | Command-line arguments |
| Pathlib | File and folder handling |
| Pandas | Excel and tabular data analysis |
| PDFPlumber | PDF text and table extraction |
| Pillow (PIL) | Image processing |
| Pytesseract | Image OCR |
| OpenCV (CV2) | Image processing and computer vision |
| NumPy | Numerical arrays and calculations |
| Regex (re) | Extract important information |
| Tabulate | Display formatted tables |
| Rich | Colourful terminal display |
| JSON | Store extracted data |
| CSV | Export extracted data |

## Project Structure
```
mini project/
├── .git
├── .venv
├── data
├── result
├── CHANGE.log
├── SYSTEM.log
├── requirements.txt
├── .gitignore
├── README.md
├── src
     ├── documind.py
     ├── extractor/
     │   ├── __init__.py
     │   ├── extractor_pdf.py
     │   ├── extractor_txt.py
     │   ├── extractor_xlsx.py
     │   └── extractor_jpg.py
     ├── converter/
     │   ├── __init__.py
     │   ├── converter_csv.py
     │   └── converter_json.py
     ├── input/
     │   └── parses.py
     ├── display/
     │   └── display.py
     │   └── display_table.py
```
## Workflow

- Accept input files and processing options through command-line arguments.

- Identify the file format and execute the appropriate extraction process.

- Clean and structure the extracted information.

- Calculate relevant statistics when applicable.

- Display the results in the terminal.

- Export the processed data to CSV or JSON.

- Save the output files in the results directory.


## Installation

- clone the repository
    git clone url(your github repository url)
- move into the project folder
    cd projectcareerzen
- Install the required libraries:
bash
pip install -r requirements.txt

## Usage

Run the following command from the project root:

```bash

- documind -f invoice.txt  --format txt --output-format csv 
- documind -f invoice.txt  --format txt --output-format json
```
bash

- documind -f documind_sample.pdf  --format pdf --output-format csv
- documind -f documind_sample.pdf  --format pdf --output-format json

bash

- documind -f markz.xlsx  --format xlsx --output-format csv
- documind -f markz.xlsx  --format xlsx --output-format json

bash

- documind -f two.jpg  --format jpg --output-format csv
- documind -f two.jpg  --format jpg --output-format json

Replace `documind_sample.pdf` with your input filename. Place input files in the `data/` directory.

## Project Structure

The project separates input handling, extraction, conversion, and display logic into dedicated modules. This modular design makes the application easier to maintain, test, and extend with additional file formats and processing features.

## Output

DocuMind stores generated files in the `results/` directory. Depending on the selected input and output format, results can include:

- Extracted text and selected fields
- File metadata
- Extracted table data
- CSV output
- JSON output

## Project Goal

DocuMind reduces manual document processing by providing a reusable command-line workflow for extracting, organizing, analyzing, and converting information from multiple file formats.


---

<div align="center">

**DocuMind — Your Document Processing Partner**

Built with Python.

</div>




