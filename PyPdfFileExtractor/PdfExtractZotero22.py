import os
import shutil
import concurrent.futures
import unicodedata
from pathlib import Path

# Define source (Zotero storage) and destination folder
source_folder = Path(r"E:\ZoteroStorage Test\ZoteroStorage")
destination_folder = Path(r"E:\ZoteroStorage Test\ZoteroPDFextractor2")

# Ensure destination folder exists
destination_folder.mkdir(parents=True, exist_ok=True)

def sanitize_filename(name):
    """Removes problematic characters from filenames."""
    return "".join(c for c in unicodedata.normalize("NFKD", name) 
                  if c.isalnum() or c in (" ", "-", "_"))

def copy_pdfs_from_folder(subfolder_path):
    """Copies PDF files from a given subfolder using threads."""
    try:
        if not subfolder_path.is_dir():
            return  # Skip if it's not a directory
            
        pdf_files = [file for file in subfolder_path.iterdir() 
                    if file.is_file() and file.suffix.lower() == ".pdf"]
        
        if not pdf_files:
            return  # Skip if no PDFs found
            
        for file in pdf_files:
            destination_path = destination_folder / file.name
            
            # Handle duplicate filenames
            counter = 1
            while destination_path.exists():
                destination_path = destination_folder / f"{file.stem}_{counter}{file.suffix}"
                counter += 1
                
            shutil.copy2(file, destination_path)
            print(f"Copied: {file} → {destination_path}")
            
    except Exception as e:
        print(f"Error processing {subfolder_path}: {e}")

def get_subfolders():
    """Return a list of subfolder paths from the source folder."""
    return [entry for entry in source_folder.iterdir() if entry.is_dir()]

# Dynamically determine the number of worker threads
num_workers = min(8, os.cpu_count() or 4)  # Use up to 8 threads
print(f"Using {num_workers} worker threads for optimized I/O.")

# Use ThreadPoolExecutor for I/O-bound tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = [executor.submit(copy_pdfs_from_folder, subfolder) 
              for subfolder in get_subfolders()]
    
    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()  # Raise any exceptions that occurred
        except Exception as e:
            print(f"Task failed: {e}")

print("✅ PDF Extraction Complete!")