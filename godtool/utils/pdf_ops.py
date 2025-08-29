from PyPDF2 import PdfMerger
import os

def merge_pdfs(folder_path, output_filename='merged.pdf'):
    """
    Merge all PDFs in folder_path into a single PDF saved as output_filename.
    """

    merger = PdfMerger()

    # List all PDF files in the folder, sorted alphabetically
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_files.sort()

    if not pdf_files:
        print(f"No PDF files found in {folder_path}")
        return

    for pdf in pdf_files:
        full_path = os.path.join(folder_path, pdf)
        print(f"Adding {pdf} ...")
        merger.append(full_path)

    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()

    print(f"Successfully merged {len(pdf_files)} PDFs into {output_path}")
