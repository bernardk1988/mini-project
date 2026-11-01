#image
from pathlib import Path
import json

def convert_json_image(metadata, extracted, text, output_file):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": metadata,
        "extracted_fields": extracted,
        "raw_text": text
    }
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"JSON saved: {output_file}")

#pdf
def convert_json_pdf(pages, metadata, output_file):
    data = {
        "metadata": metadata,
        "pages": pages
    }
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"JSON saved: {output_file.resolve()}")

#xlsx
def convert_json_xlsx(df,summery,output_file):
    output_file = Path(output_file)
    output_file.mkdir(parents=True,exist_ok=True)
    df.to_json(output_file/"processed_data.csv",orient="records",indent=4)
    with open(output_file/"summery.csv","w",encoding="utf-8") as file:
        json.dump(summery,file,indent=4)

#text

def convert_text_json(data,output_path):
    output_file =output_path / f"{output_path.stem}.json"
    with open(output_file,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
    print(f"JSON saved:{output_file}")