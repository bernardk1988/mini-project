


#xlsx

import pandas as pd
from tabulate import tabulate
from rich.console import Console
from rich.table import Table

console = Console()

def display_xlsx_data(df,summery):
    #print("\nCleaned  Tabular Data")
    #print(tabulate(df,headers="keys",tablefmt="rounded_grid",showindex=False))
    table = Table(
       title="Cleaned Tabular Data",
       border_style="red",
       header_style="bold yellow",
       show_lines=True,
    )
    for column in df.columns:
        table.add_column(str(column),justify="center",style="bold green")
    for row in df.itertuples(index=False,name=None):
        table.add_row(*[str(value) for value in row])
    console.print(table)

    print("\nSummery Statistics")
    summery_rows =[["Row Count",summery["row_count"]],["column_count",summery["column_count"]],["Highest ID",summery["highest_id"]],["Lowest ID",summery["lowest_id"]],]
    for column,value in summery["sums"].items():
         summery_rows.append([f"{column}Sum",value])
    for column,value in summery["average"].items():
         summery_rows.append([f"{column}Average",value])
    print(tabulate(
              summery_rows,
              headers=["Metric","Value"],
              tablefmt="rounded_grid",
         ))



#text

def display_txt_data(data):
     table = Table(
          title="METADATA",
          border_style="cyan",
          header_style="bold yellow",
          show_lines=True,
     )
     table.add_column("Fields",style="bold green")
     table.add_column("Value",style="white")
     for key,value in data["metadata"].items():
          table.add_row(str(key),str(value))
     console.print(table)

     # print("=====METADATA=====\n")
     # metadata_rows = [
     #      {"Fields":key,"Value":value}
     #      for key,value in data["metadata"].items()
     # ]
     # print(tabulate(
     #      metadata_rows,
     #      headers="keys",
     #      tablefmt="rounded_grid"
     # ))
     print("\n=====KEYWORDS======\n")
     keyword_rows = [
          {"keyword":key,"count":value}
          for key,value in data["keywords"].items()
     ]
     if keyword_rows:
          print(tabulate(
               keyword_rows,
               headers="keys",
               tablefmt="fancy_grid"
          ))
     else:
        print("No keywords found")

     print("\n=====EXTRACTED FIELDS=======\n")
     for key,values in data["extracted_fields"].items():
          if values:
               print(f"{key}:{','.join(values)}")
          else:
               print(f"{key}: No data found")
     print("=====EXTRACTED TEXT======")
     for page in data["pages"]:
          print(f"-----{page['page_number']}------")
          print(page["text"])