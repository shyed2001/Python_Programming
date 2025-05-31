import shutil
import concurrent.futures
import os
import unicodedata
from pathlib import Path
import logging
import time
from logging.handlers import RotatingFileHandler

# Setup logging with rotating log files to manage large logs
log_handler = RotatingFileHandler("pdf_extraction.log", maxBytes=5*1024*1024, backupCount=3)
log_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Add console handler for immediate feedback
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)

# Define source (Zotero storage) and destination folder
source_folder = Path(r"E:\ZoteroStorage Test\ZoteroStorage")
destination_folder = Path(r"E:\ZoteroStorage Test\PdfCopyZoteroMultiProcessing")

# Ensure destination folder exists
destination_folder.mkdir(parents=True, exist_ok=True)

def sanitize_filename(name):
    """Removes problematic characters from filenames."""
    return "".join(c for c in unicodedata.normalize("NFKD", name) 
                  if c.isalnum() or c in (" ", "-", "_"))

def copy_pdf(pdf_path, destination_folder, retries=3, backoff=2):
    """Copy a PDF file to the destination folder with retry logic and exponential backoff."""
    try:
        pdf_path = Path(pdf_path)
        filename = pdf_path.name
        destination_path = destination_folder / filename
        
        # Avoid overwriting by appending a number if needed
        counter = 1
        while destination_path.exists():
            name, ext = pdf_path.stem, pdf_path.suffix
            destination_path = destination_folder / f"{name}_{counter}{ext}"
            counter += 1

        # Retry logic for transient errors with exponential backoff
        for attempt in range(retries):
            try:
                shutil.copy2(pdf_path, destination_path)
                return True, pdf_path.name, destination_path.name
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed for {pdf_path.name}: {str(e)}")
                time.sleep(backoff ** attempt)  # Exponential backoff
        return False, f"Failed after {retries} attempts: {pdf_path.name}", None

    except Exception as e:
        return False, f"Error copying {pdf_path.name}: {str(e)}", None

def process_folder(subfolder_name):
    """Process all PDFs in a folder and return statistics."""
    try:
        subfolder_path = source_folder / subfolder_name
        
        if not subfolder_path.is_dir():
            return {"folder": subfolder_name, "status": "not_dir", "pdfs_found": 0, "pdfs_copied": 0}
        
        # Find all PDF files in the folder, including subdirectories
        pdf_files = []
        for item in subfolder_path.glob("**/*.pdf"):  # ** for recursive search
            if item.is_file():
                pdf_files.append(item)
        
        if not pdf_files:
            return {"folder": subfolder_name, "status": "no_pdfs", "pdfs_found": 0, "pdfs_copied": 0}
        
        # Process each PDF file
        results = []
        for pdf in pdf_files:
            success, message, new_name = copy_pdf(pdf, destination_folder)
            results.append({"file": pdf.name, "success": success, "message": message, "new_name": new_name})
        
        successful_copies = sum(1 for r in results if r["success"])
        return {
            "folder": subfolder_name,
            "status": "processed",
            "pdfs_found": len(pdf_files),
            "pdfs_copied": successful_copies,
            "details": results
        }
    except Exception as e:
        logger.error(f"Error processing folder {subfolder_name}: {e}")
        return {"folder": subfolder_name, "status": "error", "error": str(e), "pdfs_found": 0, "pdfs_copied": 0}

def main():
    start_time = time.time()
    print(f"Starting PDF extraction from {source_folder}")
    logger.info(f"Starting PDF extraction from {source_folder}")
    
    # Get all subfolders
    try:
        subfolders = [entry.name for entry in source_folder.iterdir() if entry.is_dir()]
        total_folders = len(subfolders)
        print(f"Found {total_folders} folders to process")
        logger.info(f"Found {total_folders} folders to process")
    except Exception as e:
        print(f"Error accessing source folder: {e}")
        logger.error(f"Error accessing source folder: {e}")
        return
    
    # Statistics counters
    stats = {
        "total_folders": total_folders,
        "folders_processed": 0,
        "total_pdfs_found": 0,
        "total_pdfs_copied": 0,
        "empty_folders": 0,
        "error_folders": 0
    }
    
    # Determine optimal number of workers based on 75% of available CPU
    cpu_count = os.cpu_count() or 4
    max_workers = max(1, int(cpu_count * 0.75))  # Use 75% of available CPUs, at least 1
    print(f"Using {max_workers} worker threads ({max_workers/cpu_count:.0%} of {cpu_count} CPUs)")
    logger.info(f"Using {max_workers} worker threads ({max_workers/cpu_count:.0%} of {cpu_count} CPUs)")
    
    # Process folders in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Add progress tracking
        completed = 0
        print(f"Progress: 0/{total_folders} folders processed (0%)")
        
        # Submit all tasks and collect futures
        future_to_folder = {executor.submit(process_folder, subfolder): subfolder for subfolder in subfolders}
        results = []
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_folder):
            folder_name = future_to_folder[future]
            try:
                result = future.result()
                results.append(result)
                
                # Log successful copies
                if result["status"] == "processed" and result["pdfs_copied"] > 0:
                    logger.info(f"Copied {result['pdfs_copied']}/{result['pdfs_found']} PDFs from folder '{folder_name}'")
                elif result["status"] == "error":
                    logger.error(f"Error processing folder '{folder_name}': {result.get('error', 'Unknown error')}")
                
                completed += 1
                if completed % 10 == 0 or completed == total_folders:
                    percent_done = (completed / total_folders) * 100
                    print(f"Progress: {completed}/{total_folders} folders processed ({percent_done:.1f}%)", end="\r")
                    # Also log progress to file periodically
                    if completed % 100 == 0 or completed == total_folders:
                        logger.info(f"Progress: {completed}/{total_folders} folders processed ({percent_done:.1f}%)")
            except Exception as e:
                logger.error(f"Future execution error for folder '{folder_name}': {e}")
                results.append({"folder": folder_name, "status": "error", "error": str(e), "pdfs_found": 0, "pdfs_copied": 0})
                completed += 1
    
    print("\n")  # Clear the progress line
    
    # Aggregate results
    for result in results:
        stats["folders_processed"] += 1
        
        if result["status"] == "error" or result["status"] == "not_dir":
            stats["error_folders"] += 1
        elif result["status"] == "no_pdfs":
            stats["empty_folders"] += 1
        else:
            stats["total_pdfs_found"] += result["pdfs_found"]
            stats["total_pdfs_copied"] += result["pdfs_copied"]
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60
    
    # Log results
    summary = (
        f"\n===== PDF Extraction Summary =====\n"
        f"Total folders: {stats['total_folders']}\n"
        f"Folders processed: {stats['folders_processed']}\n"
        f"Empty folders (no PDFs): {stats['empty_folders']}\n"
        f"Problem folders: {stats['error_folders']}\n"
        f"Total PDFs found: {stats['total_pdfs_found']}\n"
        f"Total PDFs copied: {stats['total_pdfs_copied']}\n"
        f"Time taken: {elapsed_minutes:.2f} minutes ({elapsed_time:.2f} seconds)\n"
        f"Processing rate: {stats['total_pdfs_copied']/elapsed_minutes:.2f} PDFs/minute\n"
        f"=================================="
    )
    
    print(summary)
    logger.info(summary)
    
    if stats['total_pdfs_found'] != stats['total_pdfs_copied']:
        print(f"WARNING: {stats['total_pdfs_found'] - stats['total_pdfs_copied']} PDFs were not copied successfully!")
        logger.warning(f"{stats['total_pdfs_found'] - stats['total_pdfs_copied']} PDFs were not copied successfully!")

    # Write a simple CSV summary for easy analysis
    try:
        with open("pdf_extraction_results.csv", "w") as f:
            f.write("Folder,Status,PDFs Found,PDFs Copied\n")
            for result in results:
                f.write(f"{result['folder']},{result['status']},{result.get('pdfs_found', 0)},{result.get('pdfs_copied', 0)}\n")
        logger.info("Results CSV file created: pdf_extraction_results.csv")
    except Exception as e:
        logger.error(f"Error creating results CSV: {e}")

if __name__ == "__main__":
    try:
        main()
        print("✅ PDF Extraction Complete!")
        logger.info("PDF Extraction Complete!")
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        logger.warning("Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in main process: {e}")
        logger.error(f"Error in main process: {e}", exc_info=True)