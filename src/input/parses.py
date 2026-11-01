

from pathlib import Path
import argparse

#pdf
from extractor.extractor_pdf import extract_textfrom_pdf
from display.display import display_pdf_data
from converter.converter_csv import converter_csv_pdf
from converter.converter_json  import convert_json_pdf

#xlsx
from extractor.extractor_xlsx import extractor_xlsx
from display.display_table import display_xlsx_data
from converter.converter_csv import converter_csv_xlsx
from converter.converter_json import convert_json_xlsx

#image
from extractor.extractor_jpg import extract_data
from display.display import display_image_data
from converter.converter_csv import convert_csv_image
from  converter.converter_json import convert_json_image

#text
from extractor.extractor_txt import extract_data12
from display.display_table import display_txt_data
from converter.converter_csv import convert_csv13
from converter.converter_json import convert_text_json



BASE_DIR=Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR /"data"
RESULT_DIR = BASE_DIR/"result"

def parse():
    parser =argparse.ArgumentParser(
        description="DocuMind Multi-Format Processing Engine"
    ) 

    parser.add_argument("-f","--file",required=True,help="Input file")
    parser.add_argument("--format",required=True,choices=["txt","xlsx","pdf","jpg"],help="File Format")
    parser.add_argument("--absolute",action="store_true",help="Display the absolute input path")
    parser.add_argument("--output-format",choices=["csv","json"],required=True,help="File Output format")

    args = parser.parse_args()
    input_path = Path(args.file)

    if not input_path.is_absolute():
        if input_path.parent == Path("."):
            input_path = DATA_DIR /input_path
        else:
            input_path= BASE_DIR/input_path
        input_path=input_path.resolve()
    RESULT_DIR.mkdir(parents=True,exist_ok=True)
    output_path = BASE_DIR / "result"
    output_file = output_path / f"{input_path.stem}.{args.output_format}"
    match args.format:
        case "txt":
            print("TXT File")
            data=extract_data12(input_path,args.format.lower().strip())
            display_txt_data(data)
            match args.output_format:
                case "csv":
                    convert_csv13(data,output_path)
                case "json":
                    convert_text_json(data,output_path)
            
        case "xlsx":
            print("XLSX File")
            df,summery = extractor_xlsx(input_path)
            display_xlsx_data(df,summery)
            match args.output_format:
                case "csv":
                    converter_csv_xlsx(df,summery,output_file)
                case "json":
                    convert_json_xlsx(df,summery,output_file)
        case "pdf":
            print("PDF File")
            pages,metadata = extract_textfrom_pdf(input_path)
            display_pdf_data(pages,metadata)
            match args.output_format:
                case "csv":
                    converter_csv_pdf(pages,metadata,output_file)
                case "json":
                    convert_json_pdf(pages, metadata, output_file)
        case "jpg" | "pdf":
            print(f"{args.format.upper()} File")
            metadata, text, extracted = extract_data(input_path)
            display_image_data(metadata, text, extracted)
            match args.output_format:
                case "csv":
                  convert_csv_image(metadata,extracted,text,output_file)
                case "json":
                  convert_json_image(metadata,extracted,text,output_file)

                
if __name__ =="__main__":
    parse()