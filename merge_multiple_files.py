import os
import pandas as pd

# Folder containing Excel files
folder_path = r"D:\InputFiles"

# Output merged file
output_file = r"D:\InputFiles\Merged_Output.xlsx"

# Get all Excel files
excel_files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".xlsx")
]

# Empty list to store DataFrames
all_data = []

# Read and append all files
for file in excel_files:
    file_path = os.path.join(folder_path, file)

    print(f"Reading: {file}")

    # Read entire Excel sheet
    df = pd.read_excel(file_path)

    # Optional: Add source file name
    df["Source_File"] = file

    # Append to list
    all_data.append(df)

# Merge all data
merged_df = pd.concat(all_data, ignore_index=True)

# Optional: Remove duplicates
merged_df.drop_duplicates(inplace=True)

# Write final merged file
merged_df.to_excel(output_file, index=False)

print(f"\nMerged file created successfully:")
print(output_file)