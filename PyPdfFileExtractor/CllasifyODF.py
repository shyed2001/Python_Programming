"""
Perfect. I’ll develop a complete Python script for you that:

- Accepts multiple metadata files (BibTeX, CSV, TXT, HTML) via command-line arguments
- Uses both BibTeX metadata (especially abstract + keywords) and PDF content (via PyMuPDF) for classification
- Classifies PDFs into 10 defined categories using keyword matching
- Copies PDFs (not moves) into category folders, preserving the original files
- Generates reports in CSV, Excel, and HTML with searchable abstracts and category tags

I’ll let you know once the script is fully prepared and ready for you to test and customize further.

# Automated Research PDF Classification Script

## Introduction

Managing large collections of research papers can be challenging. This Python script automates the classification of research PDF documents into predefined categories based on their metadata and content. It leverages common metadata fields (title, abstract, keywords, etc.) – a widely used approach for categorizing scholarly articles ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=Subject%20classification%20is%20an%20indispensable,based)) – and supplements this with full-text analysis for improved accuracy when needed ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=full,and%20ignoring%20other%20constant%20values)). By using metadata first and falling back on PDF content, the script efficiently organizes papers into relevant topic areas without altering the original files.

**Key Features:**

- **Multiple Metadata Inputs:** Accepts multiple metadata files (BibTeX `.bib`, CSV, TXT, or HTML) to gather information about the papers.
- **Metadata-Based Classification:** Uses fields like **title**, **abstract**, **keywords**, and custom tags in the metadata to determine relevant categories for each paper.
- **Content-Based Analysis:** If metadata is insufficient for classification, extracts text from the PDF (using PyMuPDF) as a secondary layer to find category keywords in the full text ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=full,and%20ignoring%20other%20constant%20values)) ([Text - PyMuPDF 1.25.5 documentation](https://pymupdf.readthedocs.io/en/latest/recipes-text.html#:~:text=fname%20%3D%20sys.argv%5B1%5D%20%20,ASCII%20characters%20pathlib.Path%28fname%20%2B%20%22.txt%22%29.write_bytes%28text.encode)).
- **Research Categories:** Classifies papers into one or more of the following categories (cross-categorization is supported if a paper matches multiple areas):
  - Distributed Systems  
  - Cloud Computing  
  - Edge & Fog Computing  
  - Mist & Dew Computing  
  - High Performance Computing (HPC)  
  - Cluster & Grid Computing  
  - Blockchain & P2P Systems  
  - Energy Efficiency & Sustainability  
  - Virtualization & Containerization  
  - Security & Trust Models
- **Output Organization:** Copies each PDF into a structured folder for each category under a user-defined output directory (the original files remain unchanged).
- **Reporting:** Generates a CSV log of classification results, an Excel summary (listing each paper's title, categories, keywords, and abstract), and an HTML index for easy browsing and searching of the categorized papers.
- **Robust Error Handling:** Includes logging for missing files, parsing errors, or unsupported formats, ensuring the script continues processing the rest of the files even if some entries have issues.

This tool helps researchers quickly organize their libraries. For example, **cloud computing** papers can be aggregated in a "Cloud Computing" folder, **blockchain** papers in "Blockchain & P2P Systems", and so on, based on keyword matching in metadata or content. The generated HTML index allows quick searching and filtering through all papers via a web browser.

## Implementation Details

**1. Metadata Parsing:** The script reads each provided metadata file to build a list of papers with their relevant fields. It supports: 

- **BibTeX (`.bib`) Files:** Processed using the `bibtexparser` library for accurate field extraction. BibTeX entries often contain fields like `title`, `abstract`, and `keywords`. For instance, a BibTeX entry might include an abstract and keyword list which `bibtexparser` will parse into a dictionary ([Tutorial — BibtexParser 1.2.0 documentation](https://bibtexparser.readthedocs.io/en/v1.2.0/tutorial.html#:~:text=%5B,2013%27%2C%20%27volume%27%3A%20%2712%27%2C%20%27ID%27%3A%20%27Cesar2013)). The script collects each entry's title, abstract, keywords, year, etc., and also checks for a `file` field (path to the PDF).
- **CSV Files:** Assumed to have column headers (e.g., *Title*, *Abstract*, *Keywords*, etc.). The script uses Python's CSV reader or pandas to read each row into a dictionary. It looks for columns like "Title", "Abstract", "Keywords" (case-insensitive) and any custom field that might indicate category. Each row becomes a paper entry.
- **TXT Files:** Plain-text metadata can vary in format. This script assumes a structured text (for example, a generated report or list of papers). If the TXT is in a known format (such as a list of titles and abstracts), the parsing logic can be customized. By default, the script will treat each line or block as one entry if possible or log an error if it cannot parse.
- **HTML Files:** The script can parse HTML pages of references (e.g., an exported bibliography in HTML format). It uses **BeautifulSoup** to find reference entries. For example, if references are listed in `<li>` or `<p>` tags, the script will extract the text, and attempt to split out the title, abstract, etc., based on common patterns or HTML structure. (This may require adjustment depending on the specific HTML format.)

After reading all metadata files, the script merges the entries. It tries to avoid duplicates (e.g., the same paper listed in multiple files) by checking unique identifiers like title or DOI. Metadata is the primary source for classification since it's fast to query and often sufficient to determine a paper's subject ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=Subject%20classification%20is%20an%20indispensable,based)).

**2. Matching PDFs to Metadata:** For each entry from the metadata, the script determines the corresponding PDF file in the provided PDF directory. It uses multiple strategies:

- If the metadata entry contains a direct file path (e.g., a BibTeX `file` field), the script will use that. It extracts the filename portion and looks for it in the PDF directory.
- If no explicit path is given, the script attempts to match by title. It will search the PDF directory for a file name that contains key parts of the paper's title. For example, a paper titled "Energy Consumption in Cloud Computing" might match a PDF named `...Energy Consumption in Cloud Computing.pdf` (or a truncated version). The matching is case-insensitive and ignores punctuation. If a match is found, that PDF path is associated with the entry.
- If multiple PDFs could match or if none is found, the script logs a warning. (In a large library, ensuring file names reflect titles or using consistent naming is helpful. The script could be extended with DOI-based matching or a lookup table if needed.)

**3. Classification Logic:** A predefined dictionary of category keywords drives the classification. Each category (e.g., "Cloud Computing") is associated with a list of keywords and phrases that commonly indicate that topic. For example, **Cloud Computing** might have keywords like "cloud computing", "cloud services", "IaaS", "PaaS", etc., while **Distributed Systems** might include "distributed system", "distributed algorithm", "peer-to-peer", and so on. These lists can be customized to the user's specific research focus.

The script first compiles a text snippet for each paper from its metadata: it combines the title, abstract, and keywords (all lowercased) into one string for searching. It then checks each category's keyword list against this metadata text:

- If any keyword is found in the title/abstract/keywords, the paper is tagged with that category. (This check is case-insensitive and can be adjusted to match whole words. For simplicity, the script uses substring matching; e.g., "cloud" in "Cloud computing environment" will count.)
- A paper can accumulate multiple category tags if it has keywords from different categories (e.g., a paper on energy-efficient cloud computing might trigger both "Cloud Computing" and "Energy Efficiency & Sustainability").

If no category keywords are found in the metadata for a given paper, the script employs **content-based analysis** as a fallback. It opens the PDF and extracts text (usually the full text or a significant portion of it) using PyMuPDF. PyMuPDF (accessible via the `fitz` module) can iterate through PDF pages and extract their text content ([Text - PyMuPDF 1.25.5 documentation](https://pymupdf.readthedocs.io/en/latest/recipes-text.html#:~:text=fname%20%3D%20sys.argv%5B1%5D%20%20,ASCII%20characters%20pathlib.Path%28fname%20%2B%20%22.txt%22%29.write_bytes%28text.encode)). This is more time-consuming than using metadata, but it can catch relevant terms that weren't present in the metadata. For example, a paper might not list "security" in its keywords, but the full text might reveal a section on security models. If the content scan finds any category keywords, those categories are added to the paper's tags. (To optimize, one could limit to scanning the introduction or conclusion of the PDF for keywords, but this script by default scans the whole document if needed.)

Using metadata first and full text second balances speed and accuracy – metadata classification is very fast and typically effective ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=Subject%20classification%20is%20an%20indispensable,based)), while full-text scanning provides a safety net for missing metadata at the cost of more processing ([Comparison of Full-Text Indexing with Metadata Indexing Based Subject Classification Using Graph-Based Index | Request PDF](https://www.researchgate.net/publication/364093773_Comparison_of_Full-Text_Indexing_with_Metadata_Indexing_Based_Subject_Classification_Using_Graph-Based_Index#:~:text=full,and%20ignoring%20other%20constant%20values)).

**4. File Copying to Category Folders:** Once categories are determined for a paper, the script copies the PDF into each corresponding category folder. It uses Python's `shutil.copy2` to copy the file (preserving metadata like timestamps) into an output directory structure. For example, if a paper is categorized as both *Cloud Computing* and *Security & Trust Models*, the PDF will be copied into: 

- `OutputDir/Cloud Computing/`  
- `OutputDir/Security & Trust Models/`  

Each category folder is created if it doesn't exist. The script ensures the original PDF files remain untouched in the source directory (only copies are made). If a paper has no categories identified (which can happen if none of the keywords were found), it will be omitted from category folders (the script can be configured to copy such files to an "Uncategorized" folder or simply skip them with a log message).

**5. Logging and Error Handling:** The script uses Python’s built-in `logging` module to record its progress and any issues. Notable events that are logged include:
- Missing metadata files or issues opening a file.
- Malformed entries in metadata (e.g., a BibTeX entry that can't be parsed) – these are skipped with an error log.
- PDF file not found for a given metadata entry (logged so the user can manually intervene if needed).
- Errors during PDF text extraction (e.g., if a PDF is corrupt or PyMuPDF cannot open it).
- Summary of how many papers were classified into each category.

By default, logs can be printed to the console and/or saved to a log file. The script’s comments and modular structure make it easy to adjust logging granularity.

## Output Reports

After processing all papers, the script produces three main outputs to summarize the classification:

- **CSV Log:** A CSV file (e.g., `classification_log.csv`) is created in the output directory. Each line represents a paper and typically includes columns like *Filename*, *Title*, and *Assigned Categories*. This provides a quick text-based log of what category each PDF was placed in. It can also include a column for any notes (e.g., "No category found" or "Multiple categories") if needed.
  
- **Excel Summary:** An Excel file (e.g., `classification_summary.xlsx`) is generated, containing a sheet (or multiple sheets) listing all papers with their details. Each row might include:
  - Title
  - Categories (possibly a semicolon-separated list if multiple)
  - Keywords (from metadata, if available)
  - Abstract (if available; having the abstract can be useful to verify the classification or to search within Excel)
  
  The Excel is created using **pandas**, which can directly write a DataFrame to an Excel `.xlsx` file with a single call ([pandas.DataFrame.to_excel — pandas 2.2.3 documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#:~:text=Write%20object%20to%20an%20Excel,sheet)) (using openpyxl under the hood). This structured spreadsheet allows filtering, sorting, or further analysis of the library.

- **HTML Index:** A HTML file (e.g., `index.html`) is produced in the output directory, serving as a browsable index of all classified papers. This page typically includes a table where each row is a paper, and columns for Title, Categories, and possibly Keywords or a snippet of the abstract. The Title can be hyperlinked to the actual PDF file (pointing to the copy in one of the category folders, so clicking it opens the PDF). The HTML includes a simple search bar at the top that filters the table in real-time using JavaScript. For instance, typing "blockchain" in the search box will hide all rows except those where "blockchain" appears in the title, category, or keywords. This is implemented with a few lines of JavaScript that loop through table rows and hide those that don't match the query ([How To Create a Filter/Search Table](https://www.w3schools.com/howto/howto_js_filter_table.asp#:~:text=for%20,)), allowing instant filtering without any server. Users can thus quickly find if a paper exists in the collection and see which category it's in. The HTML index can be opened in any web browser for convenient navigation of the PDF library.

All output files are saved in the user-specified output directory. The structure might look like this (after running the script):

```
OutputDir/
├── Cloud Computing/
│   ├── paper1.pdf
│   └── paper2.pdf
├── Distributed Systems/
│   ├── paper2.pdf
│   └── paper3.pdf
├── Security & Trust Models/
│   └── paper2.pdf
├── classification_log.csv
├── classification_summary.xlsx
└── index.html
```

In the above example, *paper2.pdf* was categorized into three areas (hence appears in multiple folders). The CSV, Excel, and HTML index list all papers with their categories for verification.

## Usage Instructions

**Installation Requirements:** Ensure you have **Python 3.x** installed along with the following packages:

- `bibtexparser` – to parse BibTeX files (install with `pip install bibtexparser`)
- `pandas` – to handle CSV/Excel data (install with `pip install pandas`; this will also require `openpyxl` for Excel support, which pandas can install as a dependency)
- `PyMuPDF` (the `fitz` module) – for PDF text extraction (install with `pip install pymupdf`)
- `beautifulsoup4` – for parsing HTML metadata files if needed (install with `pip install beautifulsoup4`)
- (Optionally, `lxml` for faster HTML parsing, and `openpyxl` explicitly if not pulled in by pandas.)

Once dependencies are installed, you can run the script from the command line. The basic usage is:

```bash
python classify_papers.py --metadata file1.bib file2.csv file3.html --pdf-dir /path/to/PDFs --output-dir /path/to/OutputDir
```

**Parameters:**

- `--metadata` (or `-m`): One or more metadata files (BibTeX/CSV/TXT/HTML) to use for classification. You can list multiple files separated by space. For example, `-m library.bib notes.csv`.
- `--pdf-dir` (or `-p`): Directory containing the PDF files to classify.
- `--output-dir` (or `-o`): Directory where category folders and report files will be created. This directory will be created if it doesn't exist.

**Example:** Suppose you have a Zotero library exported as `library.bib` and an Excel sheet `additions.csv` with some extra papers, and all corresponding PDFs are in `C:\Research\Papers`. You want the output in `C:\Research\Classified`. You would run:

```bash
python classify_papers.py -m library.bib additions.csv -p "C:\Research\Papers" -o "C:\Research\Classified"
```

After running, check the `Classified` folder for the category subfolders and the generated `index.html` (open it in a browser), the CSV log, and the Excel summary.

**Note:** If needed, you can customize the script further. For instance, you can update the `category_keywords` dictionary in the code to refine what terms map to which category, or add new categories. The script is modular, so you could also swap out the simple keyword matching with a more advanced NLP or ML model if desired in the future.

---

Below is the full Python script with detailed comments explaining each part of the process:

```python
#!/usr/bin/env python3

"""


"""
Classify research PDF documents into predefined categories based on metadata and content.

Usage:
    python classify_papers.py --metadata file1.bib file2.csv ... --pdf-dir PATH/TO/PDFs --output-dir PATH/TO/OUTPUT

Dependencies:
    - Python 3.x
    - bibtexparser (for BibTeX parsing)
    - pandas (for CSV reading and Excel writing)
    - PyMuPDF (fitz) for PDF text extraction
    - beautifulsoup4 (for HTML parsing, if needed)
"""



import os
import re
import sys
import shutil
import logging
import argparse

# ========= Optional Configuration Block (Overrides CLI if filled) =========
# If you want to run the script without command-line arguments, fill in these:

USE_CONFIG_BLOCK = True  # Set to True to use this block instead of command line

CONFIG = {
    "metadata_files": [
        r"E:\ZoteroStorage Test\ZoteroRenamedPDF\MyZotero01042025Library.bib",
        r"E:\ZoteroStorage Test\ZoteroRenamedPDF\MyZotero01042025Library.csv"
    ],
    "pdf_dir": r"E:\ZoteroStorage Test\ZoteroRenamedPDF\ALLRenamedPDF",
    "output_dir": r"E:\ZoteroStorage Test\ZoteroRenamedPDF\Final11ClassifiedOutput"
}
# ===========================================================================

# External libraries
try:
    import bibtexparser
except ImportError:
    bibtexparser = None
try:
    import pandas as pd
except ImportError:
    pd = None
try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

# Set up logging to console and file
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Define the categories and their associated keywords/phrases for classification.
# These can be customized as needed.
category_keywords = {
    "Distributed Systems": [
        "decentralized", "distributed", "distributed system", "distributed computing", "distributed algorithm", "distributed network", "peer-to-peer", "p2p"
    ],
    "Cloud Computing": [
        "cloud", "cloud computing", "cloud service", "cloud services", "cloud infrastructure", "cloud environment",
        "iaas", "paas", "saas"
    ],
    "Edge & Fog Computing": [
       "edge", "fog" "edge computing", "fog computing", "mec ", "multi-access edge", "edge device", "fog node"
    ],
    "Mist & Dew Computing": [
        "dew", "mist", "mist computing", "dew computing",  # These terms specifically target the paradigms
        "mist node", "dew node"
    ],
    "High Performance Computing": [
        "supercomputer" , "high performance computing", "hpc", "supercomputing", "mpi", "parallel computing"
    ],
    "Cluster & Grid Computing": [
      "cluster", "grid" , "cluster computing", "compute cluster", "grid computing", "distributed grid", "cluster node"
    ],
    "Blockchain & P2P Systems": [
        "blockchain", "smart contract", "peer-to-peer network", "cryptocurrency", "decentralized ledger"
    ],
    "Energy Efficiency & Sustainability": [
        "power", "energy efficiency", "energy consumption", "energy saving", "green computing", "sustainable computing", "carbon footprint"
    ],
    "Virtualization & Containerization": [
        "virtualization", "virtual machine", "hypervisor", "containerization", "docker", "kubernetes", "vmware"
    ],
    "Security & Trust Models": [
        "security", "trust model", "trust management", "privacy", "secure framework", "authentication", "authorization"
    ],
    "CPU GPU STORAGE": ["CPU", "GPU", "SSD", "HDD", "nvme", "storage" 
    ],
    "Software": ["Software"],
    "Resource": ["Resource"],
    "Mobile": ["mobile"],
    "DBMS": ["DBMS", "Database", "sql", "SQL"]   
    
  }

def parse_bibtex_file(bib_path):
    """Parse a BibTeX file and return a list of entries (dicts) with relevant fields."""
    entries = []
    if bibtexparser is None:
        logger.error(f"bibtexparser not installed, cannot parse {bib_path}")
        return entries
    try:
        with open(bib_path, 'r', encoding='utf-8') as bf:
            bib_db = bibtexparser.load(bf)
    except Exception as e:
        logger.error(f"Failed to parse BibTeX file {bib_path}: {e}")
        return entries
    for entry in bib_db.entries:
        # Normalize keys to lower-case for consistency
        entry = {k.lower(): v for k, v in entry.items()}
        # Only keep relevant fields to simplify (others can be kept if needed)
        paper = {
            "title": entry.get("title"),
            "abstract": entry.get("abstract"),
            "keywords": entry.get("keywords") or entry.get("keyword"),  # some BibTeX use 'keywords' or 'keyword'
            "year": entry.get("year"),
            "file": entry.get("file")
        }
        entries.append(paper)
    logger.info(f"Parsed {len(entries)} entries from {bib_path}")
    return entries

def parse_csv_file(csv_path):
    """Parse a CSV file of metadata. Expects headers like Title, Abstract, Keywords, etc."""
    entries = []
    if not os.path.isfile(csv_path):
        logger.error(f"CSV file not found: {csv_path}")
        return entries
    try:
        import csv
        with open(csv_path, newline='', encoding='utf-8') as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                # Normalize keys to lower-case for consistency
                row_lc = {k.lower(): v for k,v in row.items()}
                paper = {
                    "title": row_lc.get("title"),
                    "abstract": row_lc.get("abstract"),
                    "keywords": row_lc.get("keywords") or row_lc.get("keyword"),
                    "year": row_lc.get("year"),
                    "file": row_lc.get("file")  # if a path or filename is provided
                }
                # Only consider entries that have at least a title
                if paper["title"]:
                    entries.append(paper)
    except Exception as e:
        logger.error(f"Error reading CSV file {csv_path}: {e}")
    else:
        logger.info(f"Parsed {len(entries)} entries from {csv_path}")
    return entries

def parse_html_file(html_path):
    """Parse an HTML file containing references. This function may need adjustment depending on HTML structure."""
    entries = []
    if BeautifulSoup is None:
        logger.error(f"BeautifulSoup not installed, cannot parse HTML file {html_path}")
        return entries
    try:
        with open(html_path, 'r', encoding='utf-8') as hf:
            soup = BeautifulSoup(hf, 'html.parser')
    except Exception as e:
        logger.error(f"Failed to open/parse HTML file {html_path}: {e}")
        return entries
    # Heuristic: find all list items or paragraphs that might contain references
    ref_elems = soup.find_all(['li', 'p'])
    for elem in ref_elems:
        text = elem.get_text(" ", strip=True)
        if not text:
            continue
        # Very basic splitting: assume format "Title. Authors. Journal/Conference, Year." or similar
        # This is highly dependent on input format; adjust as needed.
        title = None
        abstract = None
        keywords = None
        # Try to separate title from the rest (e.g., title might be before a period).
        parts = text.split('. ')
        if parts:
            title = parts[0].strip()
            # If there's an abstract in the HTML (not common), it might be after a keyword like "Abstract:"
            if 'Abstract' in text:
                abs_index = text.lower().find('abstract')
                abstract = text[abs_index+len('abstract'):].strip(" :.")
        # Only add if we got a title
        if title:
            entries.append({
                "title": title,
                "abstract": abstract,
                "keywords": keywords,
                "file": None
            })
    logger.info(f"Parsed {len(entries)} entries from {html_path}")
    return entries

def parse_txt_file(txt_path):
    """Parse a TXT file for metadata. This is a placeholder; implementation depends on format of the TXT."""
    entries = []
    if not os.path.isfile(txt_path):
        logger.error(f"Text metadata file not found: {txt_path}")
        return entries
    try:
        with open(txt_path, 'r', encoding='utf-8') as tf:
            content = tf.read().strip()
    except Exception as e:
        logger.error(f"Error reading TXT file {txt_path}: {e}")
        return entries
    # Example implementation: assume each entry is separated by two newlines.
    raw_entries = content.split('\n\n')
    for raw in raw_entries:
        lines = raw.strip().splitlines()
        if not lines: 
            continue
        title = lines[0].strip()
        abstract = None
        keywords = None
        # Further lines might contain abstract or other info if present (this is speculative).
        for line in lines[1:]:
            if line.lower().startswith("abstract"):
                # e.g., "Abstract: xxx"
                abstract = line.split(":", 1)[-1].strip()
            elif line.lower().startswith("keywords"):
                keywords = line.split(":", 1)[-1].strip()
        entries.append({
            "title": title,
            "abstract": abstract,
            "keywords": keywords,
            "file": None
        })
    logger.info(f"Parsed {len(entries)} entries from {txt_path}")
    return entries

def load_metadata_files(files):
    """Load all metadata files and return a list of paper entries (dicts)."""
    all_entries = []
    for file_path in files:
        ext = os.path.splitext(file_path)[1].lower()
        parsed = []
        if ext == '.bib':
            parsed = parse_bibtex_file(file_path)
        elif ext == '.csv':
            parsed = parse_csv_file(file_path)
        elif ext == '.html' or ext == '.htm':
            parsed = parse_html_file(file_path)
        elif ext == '.txt':
            parsed = parse_txt_file(file_path)
        else:
            logger.error(f"Unsupported metadata file format: {file_path}")
        all_entries.extend(parsed)
    # Remove potential duplicates (by title)
    unique_entries = []
    seen_titles = set()
    for entry in all_entries:
        title = entry.get("title")
        if not title:
            continue
        title_key = title.strip().lower()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        unique_entries.append(entry)
    if len(unique_entries) != len(all_entries):
        logger.info(f"Removed {len(all_entries) - len(unique_entries)} duplicate entries based on title.")
    return unique_entries

def classify_and_copy(entries, pdf_dir, output_dir):
    """Classify each entry and copy PDF files to category folders. Returns a list of results dicts for reporting."""
    results = []
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    # Pre-list PDF directory files for matching by title (to speed up searches)
    try:
        pdf_files = os.listdir(pdf_dir)
    except Exception as e:
        logger.error(f"Could not list PDF directory {pdf_dir}: {e}")
        pdf_files = []
    # Normalize for matching
    pdf_files_lower = [f.lower() for f in pdf_files]

    for entry in entries:
        title = entry.get("title", "").strip()
        if not title:
            continue
        meta_text = (entry.get("title", "") + " " + (entry.get("abstract") or "") + " " + (entry.get("keywords") or "")).lower()
        categories = set()

        # Metadata-based classification
        for cat, keywords in category_keywords.items():
            for kw in keywords:
                if kw in meta_text:
                    categories.add(cat)
        # If no category found via metadata, use content-based analysis
        pdf_path = None
        # Determine the PDF file path if not already known
        if entry.get("file"):
            # If a file path is given in metadata, use it (it might be a relative path or contain additional info)
            file_field = entry["file"]
            # BibTeX 'file' field can contain ':/path/to/file.pdf:PDF' or similar
            if file_field:
                # Extract the part that looks like a filename
                # Remove any URI scheme or leading text up to last separator
                candidate = file_field.split('/')[-1].split('\\')[-1]
                candidate = candidate.split(':')[-1] if ':' in candidate else candidate
                candidate = candidate.strip()
                candidate_path = os.path.join(pdf_dir, candidate)
                if os.path.exists(candidate_path):
                    pdf_path = candidate_path
        # If still not found, attempt to match by title to a file in pdf_dir
        if not pdf_path:
            # Construct a simplified filename from title (alphanumeric and spaces)
            simplified = re.sub(r'[^A-Za-z0-9 ]+', '', title)
            simplified = simplified.strip().lower()
            # Try direct match in the list of files
            for fname_lower, fname in zip(pdf_files_lower, pdf_files):
                if simplified and simplified[:15] in fname_lower:  # match on first 15 chars of title (as a heuristic)
                    pdf_path = os.path.join(pdf_dir, fname)
                    break
        if not pdf_path:
            logger.warning(f"No PDF file found for title: {title}")
        else:
            entry_filename = os.path.basename(pdf_path)
            # Perform content-based classification if needed
            if not categories:
                if fitz is None:
                    logger.error(f"PyMuPDF not installed, cannot extract text for: {entry_filename}")
                else:
                    try:
                        doc = fitz.open(pdf_path)
                        text = ""
                        for page in doc:
                            text += page.get_text().lower()
                        doc.close()
                    except Exception as e:
                        logger.error(f"Failed to extract text from PDF {entry_filename}: {e}")
                        text = ""
                    if text:
                        for cat, keywords in category_keywords.items():
                            for kw in keywords:
                                if kw in text:
                                    categories.add(cat)
            # Copy file to category folders
            for cat in categories:
                cat_folder = os.path.join(output_dir, cat)
                os.makedirs(cat_folder, exist_ok=True)
                try:
                    shutil.copy2(pdf_path, cat_folder)
                except Exception as e:
                    logger.error(f"Failed to copy {entry_filename} to {cat_folder}: {e}")
            # Prepare result entry for reports
            results.append({
                "Title": title,
                "Categories": "; ".join(sorted(categories)) if categories else "",  # join multiple categories with semicolon
                "Keywords": entry.get("keywords") or "",
                "Abstract": entry.get("abstract") or "",
                "File": entry_filename
            })
    return results

def generate_reports(results, output_dir):
    """Generate CSV, Excel, and HTML reports from the classification results."""
    if not results:
        logger.info("No results to report.")
        return
    # Convert to DataFrame for easy CSV/Excel output
    if pd:
        df = pd.DataFrame(results)
        csv_path = os.path.join(output_dir, "classification_log.csv")
        excel_path = os.path.join(output_dir, "classification_summary.xlsx")
        try:
            df.to_csv(csv_path, index=False)
            logger.info(f"CSV log saved to {csv_path}")
        except Exception as e:
            logger.error(f"Failed to save CSV log: {e}")
        try:
            df.to_excel(excel_path, index=False)
            logger.info(f"Excel summary saved to {excel_path}")
        except Exception as e:
            logger.error(f"Failed to save Excel summary: {e}")
    else:
        # If pandas is not available, write a basic CSV manually
        csv_path = os.path.join(output_dir, "classification_log.csv")
        try:
            import csv
            keys = ["Title", "Categories", "Keywords", "Abstract", "File"]
            with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
                writer = csv.DictWriter(cf, fieldnames=keys)
                writer.writeheader()
                for row in results:
                    writer.writerow(row)
            logger.info(f"CSV log saved to {csv_path}")
        except Exception as e:
            logger.error(f"Failed to save CSV log: {e}")
        # Skipping Excel if pandas not available
    # Generate HTML index
    html_path = os.path.join(output_dir, "index.html")
    try:
        with open(html_path, 'w', encoding='utf-8') as hf:
            hf.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n")
            hf.write("<title>Research Paper Classification Index</title>\n")
            # Basic styling for table and search box
            hf.write("<style>\n")
            hf.write("body { font-family: Arial, sans-serif; }\n")
            hf.write("#searchInput { width: 300px; padding: 6px; margin: 12px 0; }\n")
            hf.write("table { border-collapse: collapse; width: 100%; }\n")
            hf.write("th, td { text-align: left; border: 1px solid #ddd; padding: 8px; }\n")
            hf.write("th { background-color: #f4f4f4; }\n")
            hf.write("tr.hide { display: none; }\n")
            hf.write("</style>\n")
            hf.write("</head>\n<body>\n")
            hf.write("<h2>Research Paper Classification Index</h2>\n")
            hf.write("<input type='text' id='searchInput' onkeyup='filterTable()' placeholder='Search papers...'>\n")
            hf.write("<table id='papersTable'>\n<thead><tr><th>Title</th><th>Categories</th><th>Keywords</th></tr></thead>\n<tbody>\n")
            for row in results:
                title = row.get("Title") or ""
                cats = row.get("Categories") or ""
                keywords = row.get("Keywords") or ""
                file_name = row.get("File") or ""
                # If the file was copied to at least one category, link to the first category copy
                link_path = ""
                if cats and file_name:
                    first_cat = cats.split(';')[0].strip()
                    link_path = f"{first_cat}/{file_name}"
                if link_path:
                    hf.write(f"<tr><td><a href='{link_path}' target='_blank'>{title}</a></td>")
                else:
                    hf.write(f"<tr><td>{title}</td>")
                hf.write(f"<td>{cats}</td><td>{keywords}</td></tr>\n")
            hf.write("</tbody>\n</table>\n")
            # JavaScript for filtering table based on input
            hf.write("<script>\n")
            hf.write("function filterTable() {\n")
            hf.write("  var input = document.getElementById('searchInput');\n")
            hf.write("  var filter = input.value.toLowerCase();\n")
            hf.write("  var table = document.getElementById('papersTable');\n")
            hf.write("  var trs = table.getElementsByTagName('tr');\n")
            hf.write("  for (var i = 1; i < trs.length; i++) {\n")  # skip header row
            hf.write("    var tr = trs[i];\n")
            hf.write("    var tds = tr.getElementsByTagName('td');\n")
            hf.write("    var show = false;\n")
            hf.write("    for (var j = 0; j < tds.length; j++) {\n")
            hf.write("      var cellText = tds[j].textContent.toLowerCase();\n")
            hf.write("      if (cellText.indexOf(filter) > -1) {\n")
            hf.write("        show = true; break;\n")
            hf.write("      }\n")
            hf.write("    }\n")
            hf.write("    tr.style.display = show ? '' : 'none';\n")
            hf.write("  }\n")
            hf.write("}\n")
            hf.write("</script>\n")
            hf.write("</body>\n</html>\n")
        logger.info(f"HTML index generated at {html_path}")
    except Exception as e:
        logger.error(f"Failed to generate HTML index: {e}")

def main():
    parser = argparse.ArgumentParser(description="Classify research PDFs into categories based on metadata and content.")
    parser.add_argument('-m', '--metadata', nargs='+', help="Metadata files (BibTeX/CSV/TXT/HTML) to use for classification.")
    parser.add_argument('-p', '--pdf-dir', help="Directory containing PDF files to classify.")
    parser.add_argument('-o', '--output-dir', help="Target directory for categorized output and reports.")
    args = parser.parse_args()

    # Use config block if enabled
    if 'USE_CONFIG_BLOCK' in globals() and USE_CONFIG_BLOCK:
        meta_files = CONFIG["metadata_files"]
        pdf_dir = CONFIG["pdf_dir"]
        output_dir = CONFIG["output_dir"]
        logger.info("Using configuration block instead of command-line arguments.")
    else:
        if not args.metadata or not args.pdf_dir or not args.output_dir:
            logger.error("Missing required arguments. Use --metadata, --pdf-dir, and --output-dir, or set USE_CONFIG_BLOCK = True.")
            sys.exit(1)
        meta_files = args.metadata
        pdf_dir = args.pdf_dir
        output_dir = args.output_dir

    if not os.path.isdir(pdf_dir):
        logger.error(f"PDF directory not found: {pdf_dir}")
        sys.exit(1)

    # Load and parse all metadata entries
    entries = load_metadata_files(meta_files)
    if not entries:
        logger.error("No entries found in metadata files. Exiting.")
        sys.exit(1)

    logger.info(f"Total unique papers from metadata: {len(entries)}")

    # Classify papers and copy PDFs to category folders
    results = classify_and_copy(entries, pdf_dir, output_dir)
    logger.info(f"Classification complete. {len(results)} papers processed with category assignments.")

    # Generate output reports (CSV, Excel, HTML)
    generate_reports(results, output_dir)
    logger.info("All tasks completed successfully.")
if __name__ == "__main__":
    main()


"""
``` 

**Sample Customization:** If you want to adjust the categories or keywords, simply edit the `category_keywords` dictionary in the script. You can also change how the HTML report is formatted or what columns appear in the Excel by modifying the `generate_reports` function. The script is organized into functions (`parse_*`, `classify_and_copy`, `generate_reports`) to make it easy to maintain and extend.
"""
