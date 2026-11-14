
from pathlib import Path
import pandas as pd
import json
import csv


#image

def convert_csv_image(metadata,raw_text, bill_info,output_file):
    output_file=Path(output_file)
    output_file.parent.mkdir(parents=True,exist_ok=True)
    with open(output_file,"w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow("IMAGE METADATA")
        writer.writerow(["Property","Value"])
        for key,value in metadata.items():
             writer.writerow([key,value])
        writer.writerow([])
        writer.writerow(["BILL INFORMATION"])
        writer.writerow(["Field","Value"])
        for key,value in bill_info.items():
            writer.writerow([key,value])
        writer.writerow([])
        writer.writerow("ROW OCR TEXT")
        writer.writerow(["Text"])
        writer.writerow([raw_text])
    print(f"CSV saved successfully: {output_file}")

#pdf

def converter_csv_pdf(data,output_file):
    output_file=Path(output_file)
    output_file.parent.mkdir(
        parents=True,
        exist_ok="utf-8",
    )
    with open(output_file,"w",newline="",encoding="utf-8") as file:
        Writer = csv.writer(file)
        Writer.writerow(["Category","Field","Value"])
        #meta
        for key,value in data["metadata"].items():
            Writer.writerow(["metadata",key,value])
        #impo field
        for key,value in data["extracted_fields"].items():
            Writer.writerow(["Extracted filed",key,value])
        #text
        for page in data["pages"]:
            Writer.writerow([
                "page Text", 
                f"Page {page['page_number']}",
                page["text"]
                ])
        #table
        for item in data["tables"]:
            for row_number,row in enumerate(item["data"],start=1):
                Writer.writerow([
                    "Table",
                    f"Page {item['page']} Row {row_number}",
                    "|".join(str(value or "") for value in row)
                ])
        #image
        for img in data["images"]:
            Writer.writerow(["Image",
                             f"Page {img ['page']} Image {img['image_number']}",
                             f"Width={img['width']},Height={img['height']}"
                             ])
    print(f"CSV saved:{output_file}")

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
