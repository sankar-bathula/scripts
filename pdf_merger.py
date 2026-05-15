from PyPDF2 import PdfMerger
import os

# Folder containing PDF files
pdf_folder = r"D:\PDFs"

# Output merged PDF
output_pdf = r"D:\PDFs\Merged_Output.pdf"

# Create merger object
merger = PdfMerger()

# Get all PDF files and sort them
pdf_files = sorted([
    file for file in os.listdir(pdf_folder)
    if file.endswith(".pdf")
])

# Append each PDF
for pdf in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf)

    print(f"Merging: {pdf}")

    merger.append(pdf_path)

# Write merged PDF
merger.write(output_pdf)

# Close merger
merger.close()

print("\nAll PDFs merged successfully!")
print(f"Output File: {output_pdf}")