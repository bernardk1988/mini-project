# DocuMind – Multi-Format Processing Engine

## Overview

DocuMind is a Python-based document processing tool that automates file extraction, data cleaning, analysis, and conversion. It allows users to process different file formats from the command line and export the processed results into CSV or JSON files.

## Key Features

- PDF Processing: Extracts text, metadata, and specific tables from PDF documents.

- Excel Processing: Reads XLSX files, handles missing values, and calculates summary statistics using Pandas.

- Text Processing: Extracts text, identifies target keywords, and provides document information.

- Image Processing: Uses OCR to extract text from JPG images.

- Data Analysis: Calculates row counts, sums, averages, and other relevant statistics for structured data.

- Data Conversion: Converts extracted and processed data into CSV or JSON formats.

- Terminal Display: Displays extracted data and processing summaries in a readable table format.

- File Management: Automatically locates input files and saves output files in the appropriate directories.

## Technology Stack

Python
Pandas
PDFPlumber
pdf2image
Pillow
Pytesseract
CSV and JSON
Tabulate / Rich
Argparse

## Project Structure
```
mini project/
src
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
├── CHANGE.log
├── SYSTEM.log
├── requirements.txt
└── README.md
```
## Workflow

Accept input files and processing options through command-line arguments.

Identify the file format and execute the appropriate extraction process.

Clean and structure the extracted information.

Calculate relevant statistics when applicable.

Display the results in the terminal.

Export the processed data to CSV or JSON.

Save the output files in the results directory.


## Installation

Install the required libraries:

bash
pip install -r requirements.txt

## Usage

Run the following command from the project root:

bash
documind -f studentdetails.pdf --format pdf --output-format csv/json 

Replace `studentdetails.pdf` with your input filename. Place input files in the `data/` directory.

## Project Structure

The project separates input handling, extraction, conversion, and display logic into dedicated modules. This modular design makes the application easier to maintain, test, and extend with additional file formats and processing features.

## Purpose

DocuMind reduces manual document processing by providing a reusable command-line workflow for extracting, organizing, analyzing, and converting information from multiple file formats.