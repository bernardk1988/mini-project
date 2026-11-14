
from pathlib import Path
import pandas as pd


def extractor_xlsx(input_path):
    input_path =Path(input_path)
    if input_path.suffix.lower() ==".xlsx":
        df =pd.read_excel(input_path)
    else:
        raise
    ValueError("unsuppoerted file format")

    df = df.fillna(0)
    numeric_df = df.select_dtypes(include="number")
    mark_df = numeric_df.drop(columns=["Student ID"],errors="ignore")
    summery = {
        "row_count":len(df),
        "column_count":len(df.columns),
        "sums":mark_df.sum().to_dict(),
        "average":mark_df.mean().round(2).to_dict(),
        "highest_id":(int(df["Student ID"].max()) if "Student ID" in df.columns else None),
        "lowest_id":(int(df["Student ID"].min()) if "Student ID" in df.columns else None),
                }
    return df,summery


