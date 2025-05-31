import os
import shutil
import asyncio
import aiofiles
import concurrent.futures

# Define source (Zotero storage) and destination folder
source_folder = r"E:\ZoteroStorage Test\ZoteroStorage"
destination_folder = r"E:\ZoteroStorage Test\PdfCopyZotero"

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)



async def copy_pdf_async(pdf_path, destination_folder):
    """Asynchronously copy a PDF file to the destination folder."""
    filename = os.path.basename(pdf_path)
    destination_path = os.path.join(destination_folder, filename)

    # Avoid overwriting by appending a number if needed
    counter = 1
    while os.path.exists(destination_path):
        name, ext = os.path.splitext(filename)
        destination_path = os.path.join(destination_folder, f"{name}_{counter}{ext}")
        counter += 1

    async with aiofiles.open(pdf_path, 'rb') as src, aiofiles.open(destination_path, 'wb') as dest:
        await dest.write(await src.read())  # Async file copy
    print(f"Copied: {pdf_path} → {destination_path}")



async def process_folder_async(subfolder):
    """Finds and asynchronously copies PDFs from a folder."""
    subfolder_path = os.path.join(source_folder, subfolder)
    
    if not os.path.isdir(subfolder_path):
        return  # Skip if not a directory

    pdf_files = [entry.path for entry in os.scandir(subfolder_path) if entry.is_file() and entry.name.lower().endswith(".pdf")]

    if not pdf_files:
        return  # Skip folders with no PDFs

    # Process PDFs in parallel
    await asyncio.gather(*(copy_pdf_async(pdf, destination_folder) for pdf in pdf_files))

def get_folders():
    """Returns a list of folders in source directory using os.scandir() for better performance."""
    return [entry.name for entry in os.scandir(source_folder) if entry.is_dir()]


async def main():
    subfolders = get_folders()
    # Limit concurrent tasks to prevent excessive memory usage
    batch_size = 100  # Adjust batch size based on available RAM
    for i in range(0, len(subfolders), batch_size):
        batch = subfolders[i:i + batch_size]
        await asyncio.gather(*(process_folder_async(sub) for sub in batch))


# Use a thread pool to list directories while the event loop runs
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(get_folders)
    folders = future.result()  # Run folder scanning in parallel
    asyncio.run(main())

print("✅ PDF Extraction Complete!")
