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
import csv

# Setup logging with rotating log files
log_handler = RotatingFileHandler("non_pdf_operations.log", maxBytes=5*1024*1024, backupCount=3)
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
source_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganizedPDFsV4")
destination_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\NonPDF_DestinationFolder")
duplicates_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\NonPDF_DuplicatesFolder")
report_folder = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\NonPDF_ReportFolder")

# Get current timestamp for file naming
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Ensure destination folders exist
destination_folder.mkdir(parents=True, exist_ok=True)
duplicates_folder.mkdir(parents=True, exist_ok=True)
report_folder.mkdir(parents=True, exist_ok=True)

# File to store details of non-PDF files
non_pdf_report_file = report_folder / f"non_pdf_files_report_{timestamp}.csv"

def sanitize_filename(name):
    """Removes problematic characters from filenames."""
    return "".join(c for c in unicodedata.normalize("NFKD", name) 
                  if c.isalnum() or c in (" ", "-", "_"))

def copy_file(file_path, destination_folder, retries=3, backoff=2):
    """Copy a file to the destination folder with retry logic and exponential backoff."""
    try:
        file_path = Path(file_path)
        filename = file_path.name
        destination_path = destination_folder / filename
        
        # Avoid overwriting by appending a number if needed
        counter = 1
        while destination_path.exists():
            name, ext = file_path.stem, file_path.suffix
            destination_path = destination_folder / f"{name}_{counter}{ext}"
            counter += 1

        # Retry logic for transient errors with exponential backoff
        for attempt in range(retries):
            try:
                shutil.copy2(file_path, destination_path)
                return True, file_path.name, destination_path.name
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed for {file_path.name}: {str(e)}")
                time.sleep(backoff ** attempt)  # Exponential backoff
        return False, f"Failed after {retries} attempts: {file_path.name}", None

    except Exception as e:
        logger.error(f"Error copying {file_path.name}: {str(e)}")
        return False, f"Error copying {file_path.name}: {str(e)}", None

def process_folder(subfolder_name):
    """Process all non-PDF files in a folder and return statistics."""
    try:
        subfolder_path = source_folder / subfolder_name
        
        if not subfolder_path.is_dir():
            return {"folder": subfolder_name, "status": "not_dir", "files_found": 0, "files_copied": 0}
        
        # Find all non-PDF files in the folder, including subdirectories
        non_pdf_files = []
        try:
            for item in subfolder_path.glob("**/*"):  # ** for recursive search
                if item.is_file() and item.suffix.lower() != '.pdf':
                    non_pdf_files.append(item)
        except PermissionError as e:
            logger.error(f"Permission error scanning folder {subfolder_name}: {e}")
            return {"folder": subfolder_name, "status": "permission_error", "error": str(e), "files_found": 0, "files_copied": 0}
        except Exception as e:
            logger.error(f"Error scanning for files in {subfolder_path}: {e}")
            return {"folder": subfolder_name, "status": "scan_error", "error": str(e), "files_found": 0, "files_copied": 0}
        
        if not non_pdf_files:
            return {"folder": subfolder_name, "status": "no_files", "files_found": 0, "files_copied": 0}
        
        # Process each non-PDF file
        results = []
        for file in non_pdf_files:
            success, message, new_name = copy_file(file, destination_folder)
            results.append({
                "file": file.name, 
                "path": str(file), 
                "size": file.stat().st_size, 
                "type": file.suffix, 
                "success": success, 
                "message": message, 
                "new_name": new_name
            })
        
        successful_copies = sum(1 for r in results if r["success"])
        return {
            "folder": subfolder_name,
            "status": "processed",
            "files_found": len(non_pdf_files),
            "files_copied": successful_copies,
            "details": results
        }
    except Exception as e:
        logger.error(f"Error processing folder {subfolder_name}: {e}", exc_info=True)
        return {"folder": subfolder_name, "status": "error", "error": str(e), "files_found": 0, "files_copied": 0}

def extract_non_pdf_files():
    """Extract non-PDF files from source folder to destination folder."""
    start_time = time.time()
    print(f"PHASE 1: Starting non-PDF file extraction from {source_folder}")
    logger.info(f"PHASE 1: Starting non-PDF file extraction from {source_folder}")
    
    # Get all subfolders
    try:
        subfolders = [entry.name for entry in source_folder.iterdir() if entry.is_dir()]
        total_folders = len(subfolders)
        print(f"Found {total_folders} folders to process")
        logger.info(f"Found {total_folders} folders to process")
    except PermissionError as e:
        print(f"Permission error accessing source folder: {e}")
        logger.error(f"Permission error accessing source folder: {e}")
        return False, []
    except Exception as e:
        print(f"Error accessing source folder: {e}")
        logger.error(f"Error accessing source folder: {e}", exc_info=True)
        return False, []
    
    # Statistics counters
    stats = {
        "total_folders": total_folders,
        "folders_processed": 0,
        "total_files_found": 0,
        "total_files_copied": 0,
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
    all_file_details = []
    
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
                    
                    # Collect file details for reporting
                    if "details" in result:
                        all_file_details.extend(result["details"])
                    
                    progress_bar.update(1)
                except Exception as e:
                    logger.error(f"Error processing folder '{folder_name}': {e}")
                    progress_bar.update(1)
    
    # Aggregate results
    for result in results:
        stats["folders_processed"] += 1
        
        if result["status"] == "error" or result["status"] == "not_dir":
            stats["error_folders"] += 1
        elif result["status"] == "no_files":
            stats["empty_folders"] += 1
        else:
            stats["total_files_found"] += result["files_found"]
            stats["total_files_copied"] += result["files_copied"]
    
    # Generate CSV report of all non-PDF files
    with open(non_pdf_report_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file', 'path', 'size', 'type', 'success', 'message', 'new_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for file_detail in all_file_details:
            writer.writerow({k: file_detail.get(k, '') for k in fieldnames})
    
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60
    print(f"\nTotal non-PDF files found: {stats['total_files_found']}, Total files copied: {stats['total_files_copied']}")
    print(f"Time taken: {elapsed_minutes:.2f} minutes")
    print(f"Detailed report saved to: {non_pdf_report_file}")
    
    return stats['total_files_copied'] > 0, all_file_details  # Return True if at least some files were copied

def generate_unique_name(file_path, dest_folder):
    """Generate a unique filename using a timestamp and partial hash."""
    name, ext = file_path.stem, file_path.suffix
    timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Generate a short hash of the original filename for additional uniqueness
    file_hash = sha256(name.encode()).hexdigest()[:8]
    
    unique_name = f"{name}_{timestamp_str}_{file_hash}{ext}"
    return dest_folder / unique_name

def is_duplicate(filename):
    """Check if the filename has a _N suffix indicating it's a duplicate."""
    return bool(re.search(r'_\d+\.[^.]+$', filename.lower()))

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
    """Analyze duplicate files in the destination folder and move them to duplicates folder."""
    start_time = time.time()
    print(f"\nPHASE 2: Analyzing files in {destination_folder}")
    logger.info(f"PHASE 2: Analyzing files in {destination_folder}")
    
    # Get all files
    try:
        all_files = list(destination_folder.glob("*.*"))
        total_files = len(all_files)
        print(f"Found {total_files} total files")
        logger.info(f"Found {total_files} total files")
    except Exception as e:
        logger.error(f"Error scanning destination folder: {e}", exc_info=True)
        print(f"Error scanning destination folder: {e}")
        return False
    
    # Find duplicates
    duplicates = [f for f in all_files if is_duplicate(f.name)]
    duplicate_count = len(duplicates)
    
    if duplicate_count == 0:
        print("No duplicate files found.")
        logger.info("No duplicate files found.")
        return True
    
    # Calculate percentage of duplicates
    duplicate_percentage = duplicate_count / total_files * 100 if total_files > 0 else 0
    print(f"Found {duplicate_count} duplicate files ({duplicate_percentage:.1f}% of total)")
    logger.info(f"Found {duplicate_count} duplicate files ({duplicate_percentage:.1f}% of total)")

    # Generate unique names for duplicate files and move them
    moved_count, errors = move_duplicates(duplicates)
    
    # Calculate elapsed time locally
    elapsed_time = time.time() - start_time
    elapsed_minutes = elapsed_time / 60
    
    # Print summary
    move_summary = (
        f"\n===== Duplicate Management Summary =====\n"
        f"Total files analyzed: {total_files}\n"
        f"Duplicate files found: {duplicate_count} ({duplicate_percentage:.1f}% of total)\n"
        f"Duplicates moved successfully: {moved_count} ({(moved_count/duplicate_count)*100:.1f}% success rate)\n"
        f"Failed operations: {errors}\n"
        f"Time taken: {elapsed_minutes:.4f} minutes\n"
        f"=========================================="
    )
    
    print(move_summary)
    logger.info(move_summary)

    return True

def generate_file_type_report(file_details):
    """Generate a report of file types found."""
    file_types = defaultdict(int)
    file_sizes = defaultdict(int)
    
    for file in file_details:
        file_type = file.get('type', '').lower() or 'unknown'
        file_types[file_type] += 1
        file_sizes[file_type] += file.get('size', 0)
    
    # Sort by frequency
    sorted_types = sorted(file_types.items(), key=lambda x: x[1], reverse=True)
    
    # Generate report
    report_file = report_folder / f"file_type_summary_{timestamp}.csv"
    with open(report_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Extension', 'Count', 'Total Size (bytes)', 'Average Size (bytes)'])
        
        for file_type, count in sorted_types:
            total_size = file_sizes[file_type]
            avg_size = total_size / count if count > 0 else 0
            writer.writerow([file_type, count, total_size, f"{avg_size:.2f}"])
    
    print(f"\nFile type summary report saved to: {report_file}")
    logger.info(f"File type summary report saved to: {report_file}")
    
    # Print top 10 file types
    print("\nTop file types found:")
    for i, (file_type, count) in enumerate(sorted_types[:10], 1):
        total_size_mb = file_sizes[file_type] / (1024 * 1024)
        print(f"{i}. {file_type}: {count} files ({total_size_mb:.2f} MB)")
    
    return report_file

def main():
    overall_start_time = time.time()
    script_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Starting non-PDF file extraction and duplicate management process at {script_start_time}")
    logger.info(f"Starting non-PDF file extraction and duplicate management process")
    
    # Run file extraction
    extraction_success, file_details = extract_non_pdf_files()
    if not extraction_success:
        print("File extraction failed or no files were copied, skipping duplicate analysis.")
        logger.error("File extraction failed or no files were copied, skipping duplicate analysis.")
        return
    
    # Generate file type report
    generate_file_type_report(file_details)
    
    # Run duplicate analysis and movement
    analyze_and_move_duplicates()
    
    overall_elapsed_time = time.time() - overall_start_time
    overall_elapsed_minutes = overall_elapsed_time / 60
    
    print(f"\n✅ Non-PDF file extraction and duplicate management complete!")
    print(f"Total time taken: {overall_elapsed_minutes:.2f} minutes ({overall_elapsed_time:.2f} seconds)")
    logger.info(f"Non-PDF file extraction and duplicate management complete in {overall_elapsed_minutes:.2f} minutes")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        logger.warning("Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Error in main process: {e}")
        logger.error(f"Error in main process: {e}", exc_info=True)
