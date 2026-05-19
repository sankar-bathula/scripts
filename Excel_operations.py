import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

# Output Excel file
output_file = "D://Dev_GoogleAntigravity//scripts//Data//outputs//output_report.xlsx"


# Excel file path
file_path = "D://Dev_GoogleAntigravity//scripts//Data//inputs//output.xlsx"

# Load workbook and sheet
book = load_workbook(file_path)
writer = pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay')

writer.book = book

# Select sheet
sheet = book["Sap Extract"]

# Write today's date into AC1
sheet["AC1"] = datetime.today().strftime("%m/%d/%Y")

# Save file
book.save(file_path)

print("Date written successfully in AC1")



# df_selected = df[selected_columns]

# Paste as values (write only data)
# f_selected.to_excel(output_file, index=False)
# Read entire sheet
df = pd.read_excel(file_path, sheet_name="Sap Extract")

# Copy and paste as values into new Excel file
df.to_excel(output_file, sheet_name="Sap Extract", index=False)
df = pd.read_excel(file_path, sheet_name="Sap Extract")
#Hide columns in excel
columns_to_hide = ['AF', 'AG', 'AH','AI']

for col in columns_to_hide:
    sheet.column_dimensions[col].hidden = True

print("Entire sheet copied as values successfully.")

print(f"Output File: {output_file}")
