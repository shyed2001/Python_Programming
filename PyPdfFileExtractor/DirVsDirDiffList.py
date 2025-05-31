import os
import shutil
import difflib
from pathlib import Path
import logging
from datetime import datetime
import concurrent.futures

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pdf_comparison.log"),
        logging.StreamHandler()
    ]
)

# Directory paths - replace with your actual paths
directory_1 = Path("E:\ZoteroStorage Test\ZoteroRenamedPDF\ALLRenamedPDF")  # 1650 PDFs
directory_2 = Path("E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganiedAllOutput_OrganizedPDFsV4")  # 1050 PDFs
output_directory = Path("E:\ZoteroStorage Test\ZoteroRenamedPDF\DirVsDirDiff_OrganizedPDFsV4")

# Create output directory if it doesn't exist
output_directory.mkdir(parents=True, exist_ok=True)

def get_pdf_files_with_details(directory):
    """Get all PDF files with their details from a directory."""
    pdf_files = {}
    try:
        for file_path in directory.glob("**/*.pdf"):
            if file_path.is_file():
                try:
                    pdf_files[file_path.name] = {
                        'path': file_path,
                        'size': file_path.stat().st_size,
                        'stem': file_path.stem,
                        'modified': file_path.stat().st_mtime
                    }
                except OSError as e:
                    logging.error(f"Error accessing file {file_path}: {e}")
    except Exception as e:
        logging.error(f"Error scanning directory {directory}: {e}")
    
    return pdf_files

def find_best_match(filename, target_files, threshold=0.8):
    """Find the best partial match for a filename in target_files."""
    best_match = None
    best_ratio = threshold
    
    # First check for exact stem match (ignoring extension)
    stem = Path(filename).stem
    for target_name, details in target_files.items():
        if stem == details['stem']:
            return target_name, 1.0
    
    # Then check for partial matches
    for target_name, details in target_files.items():
        ratio = difflib.SequenceMatcher(None, stem, details['stem']).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = target_name
    
    return best_match, best_ratio if best_match else 0

def is_size_match(size1, size2, tolerance=0.05):
    """Check if file sizes are within tolerance percentage."""
    if size1 == 0 or size2 == 0:
        return False
    
    size_ratio = min(size1, size2) / max(size1, size2)
    return size_ratio >= (1 - tolerance)

def copy_file(source_path, dest_dir):
    """Copy a file to destination directory with error handling."""
    try:
        dest_path = dest_dir / source_path.name
        # Avoid name collisions
        if dest_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            dest_path = dest_dir / f"{source_path.stem}_{timestamp}{source_path.suffix}"
        
        shutil.copy2(source_path, dest_path)
        return True
    except Exception as e:
        logging.error(f"Error copying {source_path}: {e}")
        return False

def process_file(filename, details, other_files, output_dir, source_dir_name):
    """Process a single file to determine if it's uncommon and copy if needed."""
    best_match, match_ratio = find_best_match(filename, other_files)
    
    # If we found a match with high similarity
    if best_match and match_ratio > 0.8:
        # Check if file sizes are similar
        size_matched = is_size_match(details['size'], other_files[best_match]['size'])
        
        if size_matched:
            # Files are similar in both name and size, not uncommon
            return None
    
    # File is uncommon - copy to output directory
    result = copy_file(details['path'], output_dir)
    if result:
        return {
            'filename': filename,
            'source': source_dir_name,
            'size': details['size'],
            'best_match': best_match,
            'match_ratio': match_ratio
        }
    return None

def main():
    start_time = datetime.now()
    logging.info(f"Starting PDF comparison at {start_time}")
    
    # Get files from both directories
    logging.info(f"Scanning directory 1: {directory_1}")
    dir1_files = get_pdf_files_with_details(directory_1)
    logging.info(f"Found {len(dir1_files)} PDF files in directory 1")
    
    logging.info(f"Scanning directory 2: {directory_2}")
    dir2_files = get_pdf_files_with_details(directory_2)
    logging.info(f"Found {len(dir2_files)} PDF files in directory 2")
    
    # Create subdirectories for each source
    output_dir1 = output_directory / "from_dir1"
    output_dir2 = output_directory / "from_dir2"
    output_dir1.mkdir(exist_ok=True)
    output_dir2.mkdir(exist_ok=True)
    
    # Process files in parallel for better performance
    uncommon_files = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        # Process files from directory 1
        future_to_file1 = {
            executor.submit(process_file, filename, details, dir2_files, output_dir1, "dir1"): filename
            for filename, details in dir1_files.items()
        }
        
        # Process files from directory 2
        future_to_file2 = {
            executor.submit(process_file, filename, details, dir1_files, output_dir2, "dir2"): filename
            for filename, details in dir2_files.items()
        }
        
        # Collect results from directory 1
        for future in concurrent.futures.as_completed(future_to_file1):
            result = future.result()
            if result:
                uncommon_files.append(result)
        
        # Collect results from directory 2
        for future in concurrent.futures.as_completed(future_to_file2):
            result = future.result()
            if result:
                uncommon_files.append(result)
    
    # Generate summary report
    uncommon_count_dir1 = sum(1 for f in uncommon_files if f['source'] == 'dir1')
    uncommon_count_dir2 = sum(1 for f in uncommon_files if f['source'] == 'dir2')
    
    logging.info(f"Found {len(uncommon_files)} uncommon files in total")
    logging.info(f"- {uncommon_count_dir1} files unique to directory 1")
    logging.info(f"- {uncommon_count_dir2} files unique to directory 2")
    
    # Write detailed report
    report_path = output_directory / "comparison_report.txt"
    with open(report_path, 'w') as f:
        f.write(f"PDF Comparison Report - {datetime.now()}\n")
        f.write(f"Directory 1: {directory_1} ({len(dir1_files)} files)\n")
        f.write(f"Directory 2: {directory_2} ({len(dir2_files)} files)\n")
        f.write(f"Total uncommon files: {len(uncommon_files)}\n")
        f.write(f"- From directory 1: {uncommon_count_dir1}\n")
        f.write(f"- From directory 2: {uncommon_count_dir2}\n\n")
        
        f.write("Detailed file list:\n")
        for file_info in sorted(uncommon_files, key=lambda x: x['source']):
            f.write(f"File: {file_info['filename']}\n")
            f.write(f"  Source: {file_info['source']}\n")
            f.write(f"  Size: {file_info['size']} bytes\n")
            if file_info['best_match']:
                f.write(f"  Best match: {file_info['best_match']} (similarity: {file_info['match_ratio']:.2f})\n")
            else:
                f.write("  No similar file found\n")
            f.write("\n")
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    logging.info(f"Comparison completed in {duration:.2f} seconds")
    logging.info(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
