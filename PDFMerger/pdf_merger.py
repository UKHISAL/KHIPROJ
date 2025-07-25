# pdf_merger.py

import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        if os.path.exists(pdf) and pdf.lower().endswith('.pdf'):
            print(f"Adding: {pdf}")
            merger.append(pdf)
        else:
            print(f"File not found or invalid: {pdf}")
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved as: {output_path}")

def get_unique_output_name(folder_path, base_name="khipropdf.pdf"):
    base, ext = os.path.splitext(base_name)
    output_path = os.path.join(folder_path, base_name)
    counter = 1
    while os.path.exists(output_path):
        output_path = os.path.join(folder_path, f"{base}{counter}{ext}")
        counter += 1
    return output_path

def main():
    print("\n📌 Please place all PDF files in the same folder.")
    folder_path = input("🔍 Enter the full path of the folder containing your PDFs: ").strip()
    file_names = input("🗂️ Enter comma-separated PDF file names (e.g., doc1.pdf, doc2.pdf): ").strip()

    if not os.path.isdir(folder_path):
        print("❌ The specified folder path does not exist.")
        return

    pdf_files = []
    for name in file_names.split(','):
        name = name.strip()
        full_path = os.path.join(folder_path, name)
        if os.path.exists(full_path):
            pdf_files.append(full_path)
        else:
            print(f"⚠️ File not found: {name}")

    if not pdf_files:
        print("❌ No valid PDF files to merge.")
        return

    output_path = get_unique_output_name(folder_path)
    merge_pdfs(pdf_files, output_path)

if __name__ == '__main__':
    main()
