import pandas as pd
import pdfplumber  # Best for table extraction

# If the PDF file is available
pdf_path = "MiniProjectDataset - MiniProjectDataset.pdf"

tables = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.extend(table)

# Convert to DataFrame
df = pd.DataFrame(tables[1:], columns=tables[0])  # Skip header row
print(df.head())

df.to_csv('customer_orders.csv',
          index=False,
          encoding='utf-8',
          sep=',',
          quotechar='"',
          quoting=1)  # 0=minimal, 1=all
print(f"DataFrame saved as 'customer_orders.csv'")
