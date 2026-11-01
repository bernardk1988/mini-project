
from pathlib import Path
import pandas as pd
import json


#image
import pandas as pd
def convert_csv_image(metadata, extracted, text, output_file):
    rows = []
    for key, value in metadata.items():
        rows.append({
            "Type": "Metadata",
            "Field": key,
            "Value": value
        })
    for key, value in extracted.items():
        rows.append({
            "Type": "Extracted Field",
            "Field": key,
            "Value": value
        })
    rows.append({
        "Type": "OCR Text",
        "Field": "Raw Text",
        "Value": text
    })
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"CSV saved: {output_file}")

#pdf
def converter_csv_pdf(pages,metadata,output_file):
    rows = []
    for key, value in metadata.items():
            rows.append({
                "Type": "Metadata",
                "Field": key,
                "Value": value
            })
    for page in pages:
            rows.append({
                "Type": "PDF Page",
                "Field": f"Page {page['page_number']}",
                "Value": page["text"]
            })
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"CSV saved: {output_file}")

#xlsx
def converter_csv_xlsx(df,summery,output_file):
     output_file = Path(output_file)
     output_file.mkdir(parents=True,exist_ok=True)
     df.to_csv(output_file/"procesed_data.csv",index=False)
     rows = [
          {
               "Matric":"Row Count","Value":summery["row_count"]
          },
          {
               "Matric":"Column Count","Value":summery["column_count"]
          },
          {
               "Matric":"Highest ID","Value":summery["highest_id"],
          },
          {
               "Matric":"Lowest ID","Value":summery["lowest_id"]
          }
     ]
     for column,value in summery["sums"].items():
          rows.append({"Matric":f"{column} Sum","Value":value})
     for column,value in summery["average"].items():
          rows.append({"Matric":f"{column} Average","Value":value})
     pd.DataFrame(rows).to_csv(output_file/"summery.csv",index=False)


#text

def convert_csv13(data, output_path):
    rows = []
    for page in data["pages"]:
        rows.append({
            **data["metadata"],
            "page_number": page["page_number"],
            "keywords": json.dumps(
                data["keywords"]
            ),
            "extracted_fields": json.dumps(
                data["extracted_fields"]
            ),
            "text": page["text"]
        })
    df = pd.DataFrame(rows)
    output_file = output_path / f"{output_path.stem}.csv"
    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )
    print(f"CSV saved: {output_file}")
