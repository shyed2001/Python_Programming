import shutil
import concurrent.futures
import os
import unicodedata
import re
from pathlib import Path
import logging
import time
from logging.handlers import RotatingFileHandler
from collections import defaultdict
from hashlib import sha256
from datetime import datetime
from tqdm import tqdm
import difflib
import hashlib

# Setup logging with rotating log files
log_handler = RotatingFileHandler("pdf_operations.log", maxBytes=5*1024*1024, backupCount=3)
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

# Define paths for all operations
source_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganizedPDFsV5")
destination_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganiedAllOutput_OrganizedPDFsV5")
duplicates_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\DuplicatesFromOrganized_OrganizedPDFsV5")

# Get current timestamp for file naming
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Ensure destination folders exist
destination_folder.mkdir(parents=True, exist_ok=True)
duplicates_folder.mkdir(parents=True, exist_ok=True)

#################################
# PDF Extraction Functions
#################################

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
        logger.error(f"Error copying {pdf_path.name}: {str(e)}")
        return False, f"Error copying {pdf_path.name}: {str(e)}", None

def process_folder(subfolder_name):
    """Process all PDFs in a folder and return statistics."""
    try:
        subfolder_path = source_folder / subfolder_name
        
        if not subfolder_path.is_dir():
            return {"folder": subfolder_name, "status": "not_dir", "pdfs_found": 0, "pdfs_copied": 0}
        
        # Find all PDF files in the folder, including subdirectories
        pdf_files = []
        try:
            for item in subfolder_path.glob("**/*.pdf"):  # ** for recursive search
                if item.is_file():
                    pdf_files.append(item)
        except PermissionError as e:
            logger.error(f"Permission error scanning folder {subfolder_name}: {e}")
            return {"folder": subfolder_name, "status": "permission_error", "error": str(e), "pdfs_found": 0, "pdfs_copied": 0}
        except Exception as e:
            logger.error(f"Error scanning for PDFs in {subfolder_path}: {e}")
            return {"folder": subfolder_name, "status": "scan_error", "error": str(e), "pdfs_found": 0, "pdfs_copied": 0}
        
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
        logger.error(f"Error processing folder {subfolder_name}: {e}", exc_info=True)
        return {"folder": subfolder_name, "status": "error", "error": str(e), "pdfs_found": 0, "pdfs_copied": 0}

def extract_pdfs():
    """Extract PDFs from Zotero storage to destination folder."""
    start_time = time.time()
    print(f"PHASE 1: Starting PDF extraction from {source_folder}")
    logger.info(f"PHASE 1: Starting PDF extraction from {source_folder}")
    
    # Get all subfolders
    try:
        subfolders = [entry.name for entry in source_folder.iterdir() if entry.is_dir()]
        total_folders = len(subfolders)
        print(f"Found {total_folders} folders to process")
        logger.info(f"Found {total_folders} folders to process")
    except PermissionError as e:
        print(f"Permission error accessing source folder: {e}")
        logger.error(f"Permission error accessing source folder: {e}")
        return False
    except Exception as e:
        print(f"Error accessing source folder: {e}")
        logger.error(f"Error accessing source folder: {e}", exc_info=True)
        return False
    
    # Statistics counters
    stats = {
        "total_folders": total_folders,
        "folders_processed": 0,
        "total_pdfs_found": 0,
        "total_pdfs_copied": 0,
        "empty_folders": 0,
        "error_folders": 0,
        "permission_error_folders": 0
    }
    
    # Determine optimal number of workers based on system resources and folder count
    cpu_count = os.cpu_count() or 4
    max_workers = max(1, cpu_count // 2)
    print(f"Using {max_workers} worker threads.")
    logger.info(f"Using {max_workers} worker threads.")
    
    # Process folders in parallel using ThreadPoolExecutor
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks and collect futures
        future_to_folder = {executor.submit(process_folder, subfolder): subfolder for subfolder in subfolders}
        
        # Process results as they complete
        with tqdm(total=total_folders, desc="Processing folders") as progress_bar:
            for future in concurrent.futures.as_completed(future_to_folder):
                folder_name = future_to_folder[future]
                try:
                    result = future.result()
                    results.append(result)
                    progress_bar.update(1)
                except Exception as e:
                    logger.error(f"Error processing folder '{folder_name}': {e}")
                    progress_bar.update(1)
    
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
    
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60
    print(f"\nTotal PDFs found: {stats['total_pdfs_found']}, Total PDFs copied: {stats['total_pdfs_copied']}")
    print(f"Time taken: {elapsed_minutes:.2f} minutes")
    
    return stats['total_pdfs_copied'] > 0  # Return True if at least some PDFs were copied

#################################
# Duplicate Analysis Functions
#################################

def is_duplicate(filename):
    """Check if the filename has a _N.pdf suffix indicating it's a duplicate."""
    return bool(re.search(r'_\d+\.pdf$', filename.lower()))

def get_original_name(filename):
    """Extract the original name without the _N suffix."""
    match = re.search(r'(.+)_\d+(\.pdf)$', filename, re.IGNORECASE)
    if match:
        return match.group(1) + match.group(2)
    return filename

def generate_unique_name(file_path, dest_folder):
    """Generate a unique filename using a timestamp and partial hash."""
    name, ext = file_path.stem, file_path.suffix
    timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Generate a short hash of the original filename for additional uniqueness
    file_hash = sha256(name.encode()).hexdigest()[:8]
    
    unique_name = f"{name}_{timestamp_str}_{file_hash}{ext}"
    return dest_folder / unique_name

def fuzzy_filename_match(filename1, filename2, threshold=0.8):
    """Compare filenames using difflib for similarity."""
    normalized1 = re.sub(r'[^a-z0-9]', '', filename1.lower())
    normalized2 = re.sub(r'[^a-z0-9]', '', filename2.lower())
    return difflib.SequenceMatcher(None, normalized1, normalized2).ratio() >= threshold

def compare_files(file1, file2):
    """Compare two files by their content using SHA-256 hash."""
    hash1 = calculate_file_hash(file1)
    hash2 = calculate_file_hash(file2)
    return hash1 == hash2

def calculate_file_hash(file_path, chunk_size=8192):
    """Calculate file hash using SHA-256."""
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(chunk_size), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def move_duplicates(duplicates):
    """Move duplicates to a new folder with unique names."""
    moved_count = 0
    errors = 0
    for dupe in duplicates:
        try:
            dest_path = generate_unique_name(dupe, duplicates_folder)
            shutil.move(dupe, dest_path)
            moved_count += 1
        except Exception as e:
            logger.error(f"Error moving duplicate file {dupe.name}: {e}")
            errors += 1
    return moved_count, errors

def analyze_and_move_duplicates():
    """Analyze duplicate PDFs in the destination folder and move them to duplicates folder."""
    start_time = time.time()
    print(f"\nPHASE 2: Analyzing PDFs in {destination_folder}")
    logger.info(f"PHASE 2: Analyzing PDFs in {destination_folder}")
    
    # Get all PDF files
    try:
        pdf_files = list(destination_folder.glob("*.pdf"))
        total_pdfs = len(pdf_files)
        print(f"Found {total_pdfs} total PDF files")
        logger.info(f"Found {total_pdfs} total PDF files")
    except Exception as e:
        logger.error(f"Error scanning destination folder: {e}", exc_info=True)
        print(f"Error scanning destination folder: {e}")
        return False
    
    # Find duplicates
    duplicates = [f for f in pdf_files if is_duplicate(f.name)]
    duplicate_count = len(duplicates)
    
    if duplicate_count == 0:
        print("No duplicate PDFs found.")
        logger.info("No duplicate PDFs found.")
        return True
    
    # Calculate percentage of duplicates
    duplicate_percentage = duplicate_count / total_pdfs * 100 if total_pdfs > 0 else 0
    print(f"Found {duplicate_count} duplicate PDF files ({duplicate_percentage:.1f}% of total)")
    logger.info(f"Found {duplicate_count} duplicate PDF files ({duplicate_percentage:.1f}% of total)")

    # Generate unique names for duplicate files and move them
    moved_count, errors = move_duplicates(duplicates)
    
    # Calculate elapsed time locally
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60
    
    # Print summary
    move_summary = (
        f"\n===== Duplicate Management Summary =====\n"
        f"Total PDFs analyzed: {total_pdfs}\n"
        f"Duplicate PDFs found: {duplicate_count} ({duplicate_percentage:.1f}% of total)\n"
        f"Duplicates moved successfully: {moved_count} ({(moved_count/duplicate_count)*100:.1f}% success rate)\n"
        f"Failed operations: {errors}\n"
        f"Time taken: {elapsed_minutes:.4f} minutes\n"
        f"=========================================="
    )
    
    print(move_summary)
    logger.info(move_summary)

    return True

#################################
# Main Function
#################################

def main():
    overall_start_time = time.time()
    script_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Starting PDF extraction and duplicate management process at {script_start_time}")
    logger.info(f"Starting PDF extraction and duplicate management process")
    
    # Run PDF extraction
    extraction_success = extract_pdfs()
    if not extraction_success:
        print("PDF extraction failed or no PDFs were copied, skipping duplicate analysis.")
        logger.error("PDF extraction failed or no PDFs were copied, skipping duplicate analysis.")
        return
    
    # Run duplicate analysis and movement
    analyze_and_move_duplicates()
    
    overall_elapsed_time = time.time() - overall_start_time
    overall_elapsed_minutes = overall_elapsed_time / 60
    
    print(f"\n✅ PDF extraction and duplicate management complete!")
    print(f"Total time taken: {overall_elapsed_minutes:.2f} minutes ({overall_elapsed_time:.2f} seconds)")
    logger.info(f"PDF extraction and duplicate management complete in {overall_elapsed_minutes:.2f} minutes")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        logger.warning("Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in main process: {e}")
        logger.error(f"Error in main process: {e}", exc_info=True)
