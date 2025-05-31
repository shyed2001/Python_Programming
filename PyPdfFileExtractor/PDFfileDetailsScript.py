import os
import datetime
import hashlib
import PyPDF2
from pathlib import Path

def get_pdf_details(file_path):
    """
    Extract detailed information from a PDF file.
    
    Args:
        file_path (str): Path to the PDF file
    
    Returns:
        dict: Dictionary containing PDF file details
    """
    try:
        # Basic file information
        file_stats = os.stat(file_path)
        
        # Calculate file hash
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        # PDF-specific information
        with open(file_path, 'rb') as f:
            try:
                pdf_reader = PyPDF2.PdfReader(f)
                
                # Extract metadata
                metadata = pdf_reader.metadata or {}
                
                # Page count
                page_count = len(pdf_reader.pages)
                
                # Try to extract text from first page for preview
                first_page_preview = ""
                try:
                    first_page_preview = pdf_reader.pages[0].extract_text()[:500] if page_count > 0 else ""
                except Exception:
                    first_page_preview = "Unable to extract page preview"
                
            except Exception as pdf_error:
                metadata = {}
                page_count = 0
                first_page_preview = f"Error reading PDF: {str(pdf_error)}"
        
        # Construct details dictionary
        pdf_details = {
            "Filename": os.path.basename(file_path),
            "Full Path": str(file_path),
            "File Size": f"{file_stats.st_size / 1024:.2f} KB",
            "Created": datetime.datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            "Last Modified": datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            "SHA256 Hash": file_hash,
            "Page Count": page_count,
            "PDF Metadata": {
                "Title": metadata.get('/Title', 'N/A'),
                "Author": metadata.get('/Author', 'N/A'),
                "Creator": metadata.get('/Creator', 'N/A'),
                "Producer": metadata.get('/Producer', 'N/A'),
                "Creation Date": metadata.get('/CreationDate', 'N/A'),
            },
            "First Page Preview": first_page_preview
        }
        
        return pdf_details
    
    except Exception as e:
        # Handle any unexpected errors
        return {
            "Filename": os.path.basename(file_path),
            "Error": str(e)
        }

def analyze_pdf_directory(directory_path, output_file='pdf_directory_analysis.txt'):
    """
    Analyze all PDF files in a given directory and save details to a text file.
    
    Args:
        directory_path (str): Path to the directory containing PDF files
        output_file (str): Name of the output text file
    """
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return
    
    # Find all PDF files
    pdf_files = list(Path(directory_path).rglob('*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files in {directory_path}")
    
    # Prepare output file
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("PDF DIRECTORY ANALYSIS\n")
        f.write(f"Analysis Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Directory: {directory_path}\n")
        f.write("=" * 50 + "\n\n")
        
        # Process each PDF file
        for idx, pdf_path in enumerate(pdf_files, 1):
            print(f"Processing file {idx}/{len(pdf_files)}: {pdf_path}")
            
            # Get PDF details
            details = get_pdf_details(pdf_path)
            
            # Write details to file
            f.write(f"FILE {idx}: {details['Filename']}\n")
            f.write("-" * 50 + "\n")
            for key, value in details.items():
                # Special handling for nested dictionaries
                if isinstance(value, dict):
                    f.write(f"{key}:\n")
                    for sub_key, sub_value in value.items():
                        f.write(f"  {sub_key}: {sub_value}\n")
                else:
                    f.write(f"{key}: {value}\n")
            f.write("\n")
    
    print(f"Analysis complete. Details saved to {output_file}")

def main():
    # Option 1: Hardcoded paths (uncomment and modify)
    directory_path = r"E:\ZoteroStorage Test\ZoteroRenamedPDF\ALLRenamedPDF" # Replace with your PDF directory path
    output_file = r"E:\ZoteroStorage Test\ZoteroRenamedPDF\ALLRenamedPDF_directory_analysis.txt"  # Replace with your desired output path
    
    # Option 2: Interactive input (comment out Option 1 and uncomment these lines)
    # directory_path = input("Enter the full path to the directory containing PDF files: ").strip()
    # output_file = input("Enter output filename (default: pdf_directory_analysis.txt): ").strip()
    # output_file = output_file if output_file else 'pdf_directory_analysis.txt'
    
    # Run analysis
    analyze_pdf_directory(directory_path, output_file)

if __name__ == '__main__':
    main()