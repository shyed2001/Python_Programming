import os
import shutil
import hashlib
import logging
import logging.handlers
import multiprocessing
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress, BarColumn, TimeElapsedColumn, MofNCompleteColumn
from typing import Generator, Tuple, Dict, Set

# --------------------------
# Configure Logging Properly
# --------------------------
log_queue = multiprocessing.Queue(-1)
queue_listener = None

def setup_logging() -> None:
    global queue_listener
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Add only queue handler to root logger
    root_logger.addHandler(logging.handlers.QueueHandler(log_queue))
    
    # Create separate handlers for the listener
    file_handler = logging.handlers.RotatingFileHandler(
        'pdf_sorter.log', maxBytes=10*1024*1024, backupCount=3, encoding='utf-8'
    )
    console_handler = logging.StreamHandler()
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Create and start queue listener
    queue_listener = logging.handlers.QueueListener(
        log_queue, file_handler, console_handler
    )
    queue_listener.start()

def stop_logging() -> None:
    if queue_listener:
        queue_listener.stop()

# --------------------------
# File Processing Utilities
# --------------------------
def file_scanner(source_dir: Path) -> Generator[Tuple[Path, int], None, None]:
    """Lazy-load PDF files with size information"""
    for file_path in source_dir.rglob('*.pdf'):
        try:
            yield (file_path, file_path.stat().st_size)
        except OSError as e:
            logging.warning(f"Skipping {file_path}: {str(e)}")
            continue

def calculate_hash(file_path: Path, chunk_size: int = 8192) -> str:
    """Safe hash calculation with progress awareness"""
    hasher = hashlib.sha256()
    try:
        with file_path.open('rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except OSError as e:
        logging.error(f"Hash calculation failed for {file_path}: {str(e)}")
        return ''

# --------------------------
# Core Processing Logic
# --------------------------
class PDFProcessor:
    def __init__(self, source_dir: Path, dest_dir: Path):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.size_map: Dict[int, Set[Path]] = defaultdict(set)
        self.file_hashes: Dict[str, Path] = {}
        self.lock = multiprocessing.Lock()
        
    def build_size_map(self) -> None:
        """Stream files to build size map without loading all paths in memory"""
        for file_path, size in file_scanner(self.source_dir):
            with self.lock:
                self.size_map[size].add(file_path)
                
    def get_unique_files(self) -> Generator[Path, None, None]:
        """Yield files with unique sizes after verification"""
        for size, paths in self.size_map.items():
            if len(paths) == 1:
                file_path = next(iter(paths))
                # Verify file still exists and size hasn't changed
                if file_path.exists() and file_path.stat().st_size == size:
                    yield file_path
                else:
                    logging.warning(f"File changed since scanning: {file_path}")

    def safe_copy(self, src_path: Path) -> Tuple[bool, str]:
        """Atomic copy with hash verification and collision handling"""
        temp_path = None  # Initialize with default value
        try:
            # Check source file integrity
            if not src_path.exists():
                return False, "Source file disappeared"
                
            file_hash = calculate_hash(src_path)
            if not file_hash:
                return False, "Hash calculation failed"
                
            # Check for existing identical file
            with self.lock:
                if existing := self.file_hashes.get(file_hash):
                    return False, f"Content duplicate of {existing}"
            
            # Atomic write procedure
            final_path = self.dest_dir / src_path.name
            
            # Handle name collisions
            counter = 1
            while final_path.exists():
                final_path = self.dest_dir / f"{src_path.stem}_{counter}{src_path.suffix}"
                counter += 1
                
            temp_path = final_path.with_name(f".tmp.{final_path.name}")
            
            # Copy to temp location first
            shutil.copy2(src_path, temp_path)
            
            # Verify temp file integrity
            if temp_path.stat().st_size != src_path.stat().st_size:
                temp_path.unlink()
                return False, "Size mismatch after copy"
                
            # Atomic rename
            temp_path.rename(final_path)
            
            # Update hash registry
            with self.lock:
                self.file_hashes[file_hash] = final_path
                
            return True, str(final_path)
            
        except Exception as e:
            # Clean up temporary files only if they exist
            if temp_path and temp_path.exists():
                try:
                    temp_path.unlink()
                except Exception as cleanup_error:
                    logging.error(f"Cleanup failed for {temp_path}: {cleanup_error}")
            return False, str(e)

# --------------------------
# Main Application Logic
# --------------------------
def process_files(processor: PDFProcessor, max_workers: int = None) -> Dict[str, list]:
    """Process files with rich progress tracking"""
    results = {'success': [], 'warnings': [], 'errors': []}
    
    with Progress(
        BarColumn(bar_width=None),
        MofNCompleteColumn(),
        "[progress.description]{task.description}",
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        # Scanning phase
        scan_task = progress.add_task("[cyan]Scanning PDF files...", total=None)
        processor.build_size_map()
        progress.remove_task(scan_task)
        
        # Prepare copying phase
        unique_files = list(processor.get_unique_files())
        copy_task = progress.add_task(
            "[green]Copying unique files...",
            total=len(unique_files),
        )
        
        # Process files with thread pool
        with ThreadPoolExecutor(
            max_workers=max_workers or (os.cpu_count() * 2)
        ) as executor:
            futures = {executor.submit(processor.safe_copy, f): f for f in unique_files}
            
            for future in as_completed(futures):
                file_path = futures[future]
                try:
                    success, message = future.result()
                    if success:
                        results['success'].append((file_path, message))
                    else:
                        results['warnings'].append((file_path, message))
                except Exception as e:
                    results['errors'].append((file_path, str(e)))
                
                progress.update(copy_task, advance=1)
                
    return results

def main() -> None:
    setup_logging()
    
    try:
        source_dir = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganiedAllOutput_OrganizedPDFsV4 - Copy")
        dest_dir = Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\UniqueSizedFiles")
        
        if not source_dir.exists():
            raise ValueError(f"Source directory not found: {source_dir}")
            
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        logging.info("Starting PDF sorting process")
        
        processor = PDFProcessor(source_dir=source_dir, dest_dir=dest_dir)
        
        results = process_files(processor=processor)
        
        logging.info("\nProcessing Summary:")
        logging.info(f"Successfully copied: {len(results['success'])}")
        logging.info(f"Warnings: {len(results['warnings'])}")
        logging.info(f"Errors: {len(results['errors'])}")
        
    except Exception as e:
        logging.critical(f"Critical failure: {str(e)}", exc_info=True)
        
    finally:
        stop_logging()

if __name__ == "__main__":
    main()
