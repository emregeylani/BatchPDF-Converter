import os
from PIL import Image
from PyPDF2 import PdfMerger

def convert_jpg_to_pdf(folder_path):
    jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]
    
    for jpg in jpg_files:
        img = Image.open(os.path.join(folder_path, jpg))
        pdf_path = os.path.join(folder_path, os.path.splitext(jpg)[0] + '.pdf')
        img.convert('RGB').save(pdf_path)
        print(f"{jpg} -> {pdf_path} olarak dönüştürüldü.")

def merge_pdfs_in_folder(folder_path):
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if len(pdf_files)==0:
        return

    pdf_files.sort()
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(os.path.join(folder_path, pdf))
    
    output_path = os.path.join(folder_path, 'OUTPUT.PDF')
    merger.write(output_path)
    merger.close()

    print(f"{folder_path} dizinindeki bütün PDF'ler {output_path} dosyasına başarıyla birleştirildi.")

def process_folders(root_folder):
    last_processed_folder = None
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if filenames:  # Sadece dosya içeren klasörleri işleyelim
            print(f"Processing folder: {dirpath}")
            convert_jpg_to_pdf(dirpath)
            merge_pdfs_in_folder(dirpath)
            last_processed_folder = dirpath
    
    if last_processed_folder:
        output_path = os.path.join(last_processed_folder, 'OUTPUT.PDF')
        print(f"Sonuç dosyası {output_path} içinde kaydedildi.")

# Kullanım
root_folder = '.'  # Ana klasör yolunu buraya gir
process_folders(root_folder)
