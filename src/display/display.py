

import pandas as pd
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel 
from rich import box

console = Console()



#pdf


def display_pdf_data(data):
     #page
     console.print(
        Panel(
            f"[bold cyan]{data['file_name']}[/bold cyan]\n"
            f"Pages: {data['page_count']}",
            title="DOCUMIND PDF PROCESSING",
            border_style="bright_blue"
        )
    )
     #meta
     meta_table = Table(
                        title="PDF METADATA",
                        box=box.ROUNDED)
     meta_table.add_column("Property",style="cyan")
     meta_table.add_column("Value",style="green")
     for key,value in data["metadata"].items():
          meta_table.add_row(str(key), str(value))
     console.print(meta_table)
    #extracted field
     field_table = Table(
        title="EXTRACTED IMPORTANT FIELDS",
        box=box.DOUBLE
    )
     field_table.add_column("Field", style="yellow")
     field_table.add_column("Value", style="bright_green")
     for key, value in data["extracted_fields"].items():
        field_table.add_row(key, str(value))
     console.print(field_table)
    #table
     console.print(
           Panel(
               f"Total tables extracted: {len(data['tables'])}",
               title="TABLE EXTRACTION",
               border_style="magenta"
           )
       )
     for item in data["tables"]:
        table = Table(
            title=f"Page {item['page']} - Table {item['table_number']}",
            box=box.SIMPLE_HEAVY
        )
        rows = item["data"]
        if rows:
            columns = max(len(row) for row in rows)

            for col in range(columns):
                table.add_column(f"Column {col + 1}")

            for row in rows:
                values = [
                    str(value or "") for value in row
                ]

                values += [""] * (columns - len(values))
                table.add_row(*values)
      #image
        image_table = Table(
        title="PDF IMAGE INFORMATION",
        box=box.ROUNDED
       )
        image_table.add_column("Page")
        image_table.add_column("Image")
        image_table.add_column("Width")
        image_table.add_column("Height")

        for img in data["images"]:
         image_table.add_row(
            str(img["page"]),
            str(img["image_number"]),
            str(img["width"]),
            str(img["height"])
        )
        console.print(image_table)
      #raw
        console.print(table)
        console.print(
        Panel(
            data["raw_text"][:5000] or "No text found",
            title="EXTRACTED RAW TEXT",
            border_style="green"
        )
    )


#image


from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box


console = Console()


def display_jpg_data(metadata,raw_text, bill_info):
   console.print(
        Panel(
            raw_text if raw_text.strip() else "No text detected",
            title="[bold cyan]RAW EXTRACTED TEXT[/bold cyan]",
            border_style="cyan",
            box=box.ROUNDED,
            style="white on grey19"
        )
    )
   metadata_table = Table(
      title="METADATA IMAGE",
      border_style="cyan",
      box =box.ROUNDED,
   )
   metadata_table.add_column("Property",style="bold green")
   metadata_table.add_column("Value",style="white")
   for key,value in metadata.items():
      metadata_table.add_row(str(key),str(value))
   console.print(metadata_table)

   bill_table = Table(
        title="EXTRACTED BILL INFORMATION",
        box=box.ROUNDED,
        border_style="green"
    )

   bill_table.add_column("Field", style="yellow")
   bill_table.add_column("Value", style="bold green")

   for key, value in bill_info.items():
        bill_table.add_row(
            key.replace("_", " ").title(),
            str(value) if value else "Not found"
        )

   console.print(bill_table)   
