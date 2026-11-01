

import pandas as pd
from tabulate import tabulate
from rich.console import Console
from rich.table import Table

console = Console()

#pdf

def display_pdf_data(pages,metadata):
#   print("\nPrint Metadata")
#   print(tabulate([{
#         "Field" :key, 
#         "value":value}
#         for key,value in metadata.items()
#     ],headers="keys",tablefmt="rounded_grid"))
   table = Table(
      title="Metadata",
      border_style="cyan",
      header_style="bold yellow",
      show_lines=True,
   )
   #console.print(table)
   table.add_column("Field",style="bold green")
   table.add_column("Value",style="white")
   for key,value in metadata.items():
      table.add_row(str(key),str(value))
   console.print(table)
   print("\nPrint Text")
   for page in pages:
    print(f"---page{page['page_number']}----")
    print(f"{page["text"]}")

#image

def display_image_data(metadata,text,extracted):
   # print("\n IMAGE / DOCUMENT METADATA")
   # print(tabulate(
   #    metadata.items(),
   #    headers=["Property","Value"],
   #    tablefmt="rounded_grid",
   # ))
   table = Table(
      title="IMAGE/DOCUMENT METADATA",
      border_style="cyan",
      header_style="bold yellow",
      show_lines=True,
   )
   table.add_column("Property",style="bold green")
   table.add_column("Value",style="white")
   for key,value in metadata.items():
      table.add_row(str(key),str(value))
   console.print(table)
   print("\nEXTRACTED FIELD")
   print(tabulate(
      extracted.items(),
      headers=["Field","Value"],
      tablefmt="rounded_grid",
   ))

   print("\n RAW TEXT")
   print(text if text.strip else 'no data found')