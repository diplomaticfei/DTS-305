import pandas as pd
import numpy as np
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

additional_countries = ["Nigeria", "NG", "U.K", "UK", "United Kingdom", "fr", "France"]

# Create a copy of the original df to extend
original_rows = len(df)

# List of new country values to shuffle with existing ones
new_countries = ["Nigeria", "NG", "U.K", "UK", "United Kingdom", "fr", "France"]

# Get current unique countries from the dataset
current_countries = df['Country'].unique().tolist()

# Combine current and new countries
all_countries = current_countries + new_countries

# Shuffle the country values randomly for each row
np.random.seed(42)
mask = np.random.random(len(df)) < 0.5  # Replace 50% of rows
df.loc[mask, 'Country'] = np.random.choice(new_countries, size=mask.sum(), replace=True)

# Show the updated unique countries
print("Updated unique countries in dataset:")
print(df['Country'].unique())


df.to_csv('customer_orders.csv',
          index=False,
          encoding='utf-8',
          sep=',',
          quotechar='"',
          quoting=1)  # 0=minimal, 1=all
print(f"DataFrame saved as 'customer_orders.csv'")
