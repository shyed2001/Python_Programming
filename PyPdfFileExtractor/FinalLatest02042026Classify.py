import os
import re
import csv
import time
import logging
import hashlib
import bibtexparser
import pandas as pd
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from collections import defaultdict
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding
from PyPDF2 import PdfReader
import fitz  # PyMuPDF
import shutil
from rapidfuzz import fuzz, process

# Configuration
CONFIG = {
    "source_dir": Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\ALLRenamedPDF"),
    "output_dir": Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\OrganizedPDFsV5"),
    "bibtex_files": [Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\No.bib")],
    "csv_files": [Path(r"E:\ZoteroStorage Test\ZoteroRenamedPDF\No.csv")],
    "log_file": "pdf_processing.log",
    "categories": {
        "Distributed Systems": [
            "decentralized", "distributed", "distributed system", "distributed computing",
            "distributed algorithm", "distributed network" ],
        "Cloud Computing": [
            "cloud", "cloud computing", "cloud service", "cloud services",
            "cloud infrastructure", "cloud environment", "iaas", "paas", "saas"
        ],
        "Edge & Fog Computing": [
            "edge", "fog", "edge computing", "fog computing", "mec ",
            "multi-access edge", "edge device", "fog node"
        ],
        "Mist & Dew Computing": [
            "dew", "mist", "mist computing", "dew computing",
            "mist node", "dew node"
        ],
        "High Performance Computing": [
            "supercomputer", "high performance computing", "hpc",
            "supercomputing", "mpi", "parallel computing"
        ],
        "Cluster & Grid Computing": [
            "cluster", "grid", "cluster computing", "compute cluster",
            "grid computing", "distributed grid", "cluster node"
        ],
        "Blockchain": [
            "blockchain", "smart contract", "peer-to-peer network",
            "cryptocurrency", "decentralized ledger"
        ],
        "Energy Efficiency & Sustainability": [
            "power", "energy efficiency", "energy consumption", "energy saving",
            "green computing", "sustainable computing", "carbon footprint"
        ],
        "Virtualization Sandbox Containerization": [
            "virtualization", "virtual machine", "hypervisor",
            "containerization", "docker", "kubernetes", "vmware" "containers" "sandbox"
        ],
        "Security & Trust Models": [
            "security", "trust model", "trust management", "privacy",
            "secure framework", "authentication", "authorization"
        ],
        "CPU GPU STORAGE": [
            "CPU", "GPU", "SSD", "HDD", "nvme", "storage"
        ],
        "Software": ["Software", "code"],
        "Mobile": ["mobile"],
        "DBMS": ["dbms", "database", "sql", "relational", "nosql"
],
   "Study Review Survey": [
    "review", "survey", "study" , "meta-analysis", "overview", "state-of-the-art",
    "study review", "literature review", "systematic review"
],
"Resource Management Allocation Scheduling": [
    "resource management", "resource allocation", "resource discovery",
    "orchestration", "load balancing", "task scheduling", "scheduling", "resource usage", "availability"
],
"System Performance & Benchmarking": [
    "performance", "benchmark", "benchmarking", "latency",
    "throughput", "speedup", "efficiency"
], "Torrent & P2P Sharing": [
    "torrent", "peer-to-peer sharing", "bitTorrent", "peer sharing",
    "distributed sharing", "file sharing", "p2p network", "Torrent"
],
        "Education & Learning Technologies": [
    "education", "e-learning", "learning management", "online learning",
    "intelligent tutoring", "mooc", "learning platform", "edtech"
],
        "Healthcare & Biomedical": [
    "healthcare", "biomedical", "telemedicine", "medical image",
    "health monitoring", "ehealth", "clinical", "diagnosis", "patient data"
],
        "Ethics & Fairness": [
    "bias", "fairness", "ethics", "accountability", "explainability",
    "transparency", "responsible ai", "discrimination", "ai ethics"
],
        "Data Science & Analytics": [
    "data science", "data analysis", "big data", "data mining",
    "analytics", "visualization", "predictive", "statistical", "exploratory"
],
        "Networking & Protocols": [
    "network", "protocol", "communication protocol", "wireless",
    "tcp", "udp", "5g", "lte", "routing", "bandwidth", "networking"
],
        "Simulation & Modeling": [
    "simulation", "simulator", "modeling", "model-based", "analytical model",
    "agent-based model", "discrete-event", "virtual testbed"
],
        "IoT & Cyber-Physical Systems": [
    "iot", "cyber-physical", "smart devices", "smart home", "sensor network",
    "wearables", "embedded system", "cyber physical", "actuator", "ubiquitous"
],
        "Artificial Intelligence & Machine Learning": [
    "machine learning", "deep learning", "neural network", "ai",
    "artificial intelligence", "reinforcement learning", "classification", "supervised", "unsupervised",
    "cnn", "rnn", "transformer", "attention", "ml", "gan"
],

        "Uncategorized":[]
    },
    "fuzzy_match_threshold": 80,  # Minimum score (0-100) for fuzzy matching
    "num_workers": os.cpu_count() or 4
}

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CONFIG['log_file']),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MetadataIndex:

    def __init__(self):
        self.bibtex_entries = defaultdict(dict)
        self.csv_entries = defaultdict(dict)
        
        # Title-to-metadata lookup
        self.title_to_metadata = {}
        
        # Author+Year lookup for matching filenames
        self.author_year_lookup = {}
        
        # All titles for reverse lookup
        self.all_titles = []
    
    def load_bibtex(self, file_path: Path):
        """Load and parse BibTeX files with enhanced metadata extraction"""
        with open(file_path, encoding='utf-8') as bibtex_file:
            parser = BibTexParser(common_strings=True)
            parser.customization = homogenize_latex_encoding
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
            for entry in bib_database.entries:
                clean_entry = {k.lower(): v for k, v in entry.items()}
                title = clean_entry.get('title', '').lower()
                
                if title:
                    self.bibtex_entries[title] = clean_entry
                    self.title_to_metadata[title] = {
                        'title': title,
                        'authors': clean_entry.get('author', ''),
                        'year': clean_entry.get('year', ''),
                        'abstract': clean_entry.get('abstract', ''),
                        'keywords': clean_entry.get('keywords', ''),
                        'source': 'bibtex'
                    }
                    
                    # Store title for reverse matching
                    self.all_titles.append(title)
                    
                    # Create author+year keys for matching
                    author = clean_entry.get('author', '')
                    year = clean_entry.get('year', '')
                    if author and year:
                        # Extract first author's last name
                        author_parts = author.split(' and ')[0].split(',')
                        if author_parts:
                            last_name = author_parts[0].strip().lower()
                            # Create common author+year patterns
                            key1 = f"{last_name}{year}".lower()  # smith2023
                            key2 = f"{last_name}_{year}".lower()  # smith_2023
                            key3 = f"{year}_{last_name}".lower()  # 2023_smith
                            
                            for key in [key1, key2, key3]:
                                self.author_year_lookup[key] = title
    
    def load_csv(self, file_path: Path):
        """Load and parse CSV metadata files with enhanced metadata extraction"""
        try:
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                row_dict = row.to_dict()
                
                # Normalize keys to lowercase
                row_dict = {k.lower(): v for k, v in row_dict.items()}
                
                title = row_dict.get('title', '').lower()
                if title:
                    self.csv_entries[title] = row_dict
                    self.title_to_metadata[title] = {
                        'title': title,
                        'authors': row_dict.get('author', row_dict.get('authors', '')),
                        'year': row_dict.get('year', row_dict.get('date', '')),
                        'abstract': row_dict.get('abstract', ''),
                        'keywords': row_dict.get('keywords', row_dict.get('tags', '')),
                        'source': 'csv'
                    }
                    
                    # Store title for reverse matching
                    self.all_titles.append(title)
                    
                    # Create author+year keys for matching
                    author = row_dict.get('author', row_dict.get('authors', ''))
                    year = row_dict.get('year', row_dict.get('date', ''))
                    if author and year:
                        # Handle different CSV author formats
                        if ',' in author:
                            last_name = author.split(',')[0].strip().lower()
                        else:
                            last_name = author.split()[-1].lower()
                        
                        # Create author+year patterns
                        key1 = f"{last_name}{year}".lower()
                        key2 = f"{last_name}_{year}".lower()
                        key3 = f"{year}_{last_name}".lower()
                        
                        for key in [key1, key2, key3]:
                            self.author_year_lookup[key] = title
        except Exception as e:
            logger.error(f"Error loading CSV {file_path}: {e}")


class PDFProcessor:

    def __init__(self, metadata_index: MetadataIndex):
        self.metadata_index = metadata_index
        self.file_hashes = set()
        self.results = []
        
        # Cache of all filenames in source_dir for matching
        self.all_filenames = []
        self.load_source_files()
    
    def load_source_files(self):
        """Load all filenames from source directory for matching"""
        try:
            for file in CONFIG['source_dir'].glob('*.pdf'):
                self.all_filenames.append(file.name)
        except Exception as e:
            logger.error(f"Error loading source files: {e}")
    
    def process_pdf(self, pdf_path: Path):
        """Main PDF processing workflow with enhanced matching"""
        try:
            file_hash = self._compute_hash(pdf_path)
            if file_hash in self.file_hashes:
                return
            self.file_hashes.add(file_hash)
            
            # Extract basic PDF metadata
            pdf_metadata = self._extract_pdf_metadata(pdf_path)
            
            # Enhanced matching to find the correct metadata
            match_result = self._match_pdf_to_metadata(pdf_path, pdf_metadata)
            match_type = match_result['match_type']
            external_metadata = match_result['metadata']
            
            # Combine metadata
            combined_metadata = {**pdf_metadata, **external_metadata}
            combined_metadata['match_type'] = match_type
            
            # Only extract text if needed for classification
            text_content = ""
            
            # Classify document
            categories = self._classify_document(combined_metadata, text_content)
            
            # Only extract text if no categories were found and we need content-based classification
            if not categories:
                text_content = self._extract_text(pdf_path)
                categories = self._classify_document(combined_metadata, text_content)
            
            # Save to output folders
            self._save_to_output(pdf_path, categories, combined_metadata)
            
            # Create result entry for reports
            self.results.append(
                self._create_result_row(pdf_path, categories, combined_metadata)
            )
            
        except Exception as e:
            logger.error(f"Error processing {pdf_path}: {e}")
    
    def _compute_hash(self, pdf_path: Path) -> str:
        """Compute SHA-256 hash of file content"""
        hasher = hashlib.sha256()
        with open(pdf_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def _extract_pdf_metadata(self, pdf_path: Path) -> Dict:
        """Extract metadata from PDF file"""
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            info = reader.metadata or {}
            return {
                'title': info.get('/Title', pdf_path.stem),
                'author': info.get('/Author', ''),
                'keywords': info.get('/Keywords', ''),
                'creation_date': info.get('/CreationDate', '')
            }
    
    def _match_pdf_to_metadata(self, pdf_path: Path, pdf_metadata: Dict) -> Dict:
        """
        Enhanced matching logic using multiple strategies:
        1. Direct title match
        2. Fuzzy title match
        3. Author+Year match
        4. Reverse fuzzy match (filename to metadata)
        
        Returns a dict with match_type and metadata
        """
        result = {
            'match_type': 'Unmatched',
            'metadata': {
                'bibtex': {},
                'csv': {}
            }
        }
        
        filename = pdf_path.name
        pdf_title = pdf_metadata['title'].lower() if pdf_metadata['title'] else ''
        
        # Strategy 1: Direct title match
        if pdf_title and pdf_title in self.metadata_index.title_to_metadata:
            metadata_title = pdf_title
            match_type = 'Direct Match'
            logger.info(f"Direct title match for {filename}: {metadata_title}")
            
            title_metadata = self.metadata_index.title_to_metadata[metadata_title]
            source = title_metadata['source']
            
            if source == 'bibtex':
                result['metadata']['bibtex'] = self.metadata_index.bibtex_entries[metadata_title]
            elif source == 'csv':
                result['metadata']['csv'] = self.metadata_index.csv_entries[metadata_title]
            
            result['match_type'] = match_type
            return result
        
        # Strategy 2: Fuzzy title match
        if pdf_title:
            # Get the closest match with score
            matches = process.extractOne(
                pdf_title,
                self.metadata_index.all_titles,
                scorer=fuzz.token_sort_ratio
            )
            
            if matches and matches[1] >= CONFIG['fuzzy_match_threshold']:
                metadata_title = matches[0]
                match_type = 'Fuzzy Match'
                logger.info(f"Fuzzy title match for {filename}: {metadata_title} (score: {matches[1]})")
                
                title_metadata = self.metadata_index.title_to_metadata[metadata_title]
                source = title_metadata['source']
                
                if source == 'bibtex':
                    result['metadata']['bibtex'] = self.metadata_index.bibtex_entries[metadata_title]
                elif source == 'csv':
                    result['metadata']['csv'] = self.metadata_index.csv_entries[metadata_title]
                
                result['match_type'] = match_type
                return result
        
        # Strategy 3: Author+Year match
        filename_base = pdf_path.stem.lower()  # Get filename without extension
        
        # Extract potential author+year patterns from filename
        # Try various patterns like "smith2023", "smith_2023", "2023_smith"
        for pattern_key in self.metadata_index.author_year_lookup.keys():
            if pattern_key in filename_base:
                metadata_title = self.metadata_index.author_year_lookup[pattern_key]
                match_type = 'Author+Year Match'
                logger.info(f"Author+Year match for {filename}: {metadata_title} via pattern {pattern_key}")
                
                title_metadata = self.metadata_index.title_to_metadata[metadata_title]
                source = title_metadata['source']
                
                if source == 'bibtex':
                    result['metadata']['bibtex'] = self.metadata_index.bibtex_entries[metadata_title]
                elif source == 'csv':
                    result['metadata']['csv'] = self.metadata_index.csv_entries[metadata_title]
                
                result['match_type'] = match_type
                return result
        
        # Strategy 4: Reverse fuzzy match (match filename to closest title)
        # This helps with heavily truncated or modified filenames
        matches = process.extractOne(
            filename_base,
            self.metadata_index.all_titles,
            scorer=fuzz.token_set_ratio  # More lenient for filenames
        )
        
        if matches and matches[1] >= CONFIG['fuzzy_match_threshold']:
            metadata_title = matches[0]
            match_type = 'Reverse Fuzzy Match'
            logger.info(f"Reverse fuzzy match for {filename}: {metadata_title} (score: {matches[1]})")
            
            title_metadata = self.metadata_index.title_to_metadata[metadata_title]
            source = title_metadata['source']
            
            if source == 'bibtex':
                result['metadata']['bibtex'] = self.metadata_index.bibtex_entries[metadata_title]
            elif source == 'csv':
                result['metadata']['csv'] = self.metadata_index.csv_entries[metadata_title]
            
            result['match_type'] = match_type
            return result
        
        # If we get here, no match was found
        logger.warning(f"No metadata match found for {filename}")
        return result
    
    def _extract_text(self, pdf_path: Path) -> str:
        """Extract text content using PyMuPDF"""
        try:
            doc = fitz.open(pdf_path)
            return " ".join(page.get_text() for page in doc)
        except Exception as e:
            logger.warning(f"Text extraction failed for {pdf_path}: {e}")
            return ""
    
    def _classify_document(self, metadata: Dict, text: str) -> List[str]:
        """
        Classify document based on multiple criteria with priority order:
        1. Title and filename text matching
        2. Keywords in metadata
        3. Abstract in metadata
        4. Full PDF content
        """
        categories = defaultdict(int)
        match_type = metadata.get('match_type', 'Unmatched')
        
        # 1. Check title & filename for direct keyword matches (highest priority)
        title = metadata['title'].lower() if metadata['title'] else ''
        if title:
            for category, keywords in CONFIG['categories'].items():
                if any(re.search(rf'\b{re.escape(kw)}\b', title) for kw in keywords):
                    categories[category] += 3  # Higher weight for direct title matches
        
        # 2. Check all external metadata fields
        for source in ['bibtex', 'csv']:
            for field, value in metadata.get(source, {}).items():
                if isinstance(value, str):
                    # Give higher weight to keyword/abstract fields
                    weight = 2 if field.lower() in ['keywords', 'keyword', 'tags', 'abstract'] else 1
                    
                    for category, keywords in CONFIG['categories'].items():
                        categories[category] += sum(
                            weight for kw in keywords if kw.lower() in value.lower()
                        )
        
        # 3. Only use text content if no strong category matches from metadata
        if not categories or max(categories.values()) < 3:
            if text:  # If text content was provided or extracted
                for category, keywords in CONFIG['categories'].items():
                    if any(re.search(rf'\b{re.escape(kw)}\b', text.lower()) for kw in keywords):
                        categories[category] += 1  # Lower weight for text content matches
        
        # Return top categories with highest scores
       # return sorted(categories.keys(), key=categories.get, reverse=True)[:3] if categories else []
            # Return top categories with highest scores
        return sorted(categories.keys(), key=categories.get, reverse=True)[:3] if categories else ['Uncategorized']
    
    def _save_to_output(self, pdf_path: Path, categories: List[str], metadata: Dict):
        """Save PDF to categorized folders"""
        primary_category = categories[0] if categories else 'Uncategorized'
        dest_dir = CONFIG['output_dir'] / primary_category
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename from metadata
        match_type = metadata.get('match_type', 'Unmatched')
        
        if match_type != 'Unmatched':
            # Use metadata for filename if we have a match
            if 'bibtex' in metadata and metadata['bibtex']:
                authors = metadata['bibtex'].get('author', 'Unknown')
            elif 'csv' in metadata and metadata['csv']:
                authors = metadata['csv'].get('author', metadata['csv'].get('authors', 'Unknown'))
            else:
                authors = metadata['author'] if metadata['author'] else 'Unknown'
        else:
            # Use PDF metadata if no match
            authors = metadata['author'] if metadata['author'] else 'Unknown'
        
        # Clean up author names
        if 'and' in authors:
            # Handle BibTeX style multiple authors
            first_author = authors.split(' and ')[0]
            if ',' in first_author:
                clean_authors = first_author.split(',')[0].strip()
            else:
                clean_authors = first_author.split()[-1].strip()
        elif ',' in authors:
            # Handle CSV style author lists
            clean_authors = authors.split(',')[0].strip()
        else:
            clean_authors = authors.split()[-1].strip() if authors != 'Unknown' else 'Unknown'
        
        # Remove problematic characters
        clean_authors = re.sub(r'[\\/*?:"<>|]', '', clean_authors)
        
        """         
        new_filename = f"{clean_authors} - {metadata['title']} [{match_type}].pdf"
        
        dest_path = dest_dir / new_filename
        shutil.copy2(pdf_path, dest_path) """
        base_title = metadata['title'].strip()
# Only include author if it's known (not 'Unknown')
        if clean_authors.lower() != 'unknown':
            new_filename = f"{clean_authors} - {base_title}.pdf"
        else:
            new_filename = f"{base_title}.pdf"
            
        dest_path = dest_dir / new_filename
        shutil.copy2(pdf_path, dest_path)    
        # Create filename with match type info

        

           
            
    
    
def _create_result_row(self, pdf_path: Path, categories: List[str], metadata: Dict) -> Dict:
        """Create result entry for reporting with match type information"""
        return {
            'original_path': str(pdf_path),
            'title': metadata['title'],
            'authors': metadata['author'],
            'categories': ', '.join(categories),
            'keywords': metadata['keywords'],
            'match_type': metadata.get('match_type', 'Unmatched'),
            'bibtex_fields': ', '.join(metadata.get('bibtex', {}).keys()),
            'csv_fields': ', '.join(metadata.get('csv', {}).keys()),
            'creation_date': metadata['creation_date']
        }


def generate_reports(results: List[Dict]):
    """Generate CSV, Excel, and HTML reports with match type information"""
    df = pd.DataFrame(results)
    
    # CSV Report
    csv_path = CONFIG['output_dir'] / "classification_report.csv"
    df.to_csv(csv_path, index=False)
    
    # Excel Report
    excel_path = CONFIG['output_dir'] / "classification_report.xlsx"
    with pd.ExcelWriter(excel_path) as writer:
        df.to_excel(writer, index=False)
        
        # Add a summary sheet with match type statistics
        match_counts = df['match_type'].value_counts().reset_index()
        match_counts.columns = ['Match Type', 'Count']
        match_counts.to_excel(writer, sheet_name='Match Summary', index=False)
        
        # Add a category summary sheet
        category_stats = []
        for category in CONFIG['categories'].keys():
            count = df[df['categories'].str.contains(category, na=False)].shape[0]
            category_stats.append({'Category': category, 'Count': count})
        
        category_df = pd.DataFrame(category_stats)
        category_df.to_excel(writer, sheet_name='Category Summary', index=False)
    
    # HTML Report with match type information
    html_path = CONFIG['output_dir'] / "classification_dashboard.html"
    html_template = f"""
    <html><head><title>PDF Classification Report</title>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    <style>
    .match-direct {{ background-color: #d4edda; }}
    .match-fuzzy {{ background-color: #fff3cd; }}
    .match-author {{ background-color: #d1ecf1; }}
    .match-reverse {{ background-color: #f8d7da; }}
    .match-unmatched {{ background-color: #e2e3e5; }}
    </style>
    </head><body>
    <h1>PDF Classification Report - {datetime.now().strftime('%Y-%m-%d')}</h1>
    
    <h2>Match Type Summary</h2>
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th>Match Type</th>
          <th>Count</th>
          <th>Percentage</th>
        </tr>
      </thead>
      <tbody>
    """
    
    # Add match type statistics
    match_counts = df['match_type'].value_counts()
    total = len(df)
    for match_type, count in match_counts.items():
        percentage = (count / total) * 100
        html_template += f"<tr><td>{match_type}</td><td>{count}</td><td>{percentage:.1f}%</td></tr>\n"
    
    html_template += """
      </tbody>
    </table>
    
    <h2>Detailed Report</h2>
    """
    
    # Convert main DataFrame to HTML with styling for match types
    df_html = df.to_html(table_id='reportTable', classes='display', escape=False)
    
    # Add match type styling with JavaScript
    html_template += df_html
    html_template += """
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
    <script>
    $(document).ready(function() {
        var table = $('#reportTable').DataTable();
        
        // Add classes based on match type
        $('#reportTable tbody tr').each(function() {
            var matchType = $(this).find('td:contains("Direct Match")').length > 0 ? 'direct' : 
                            $(this).find('td:contains("Fuzzy Match")').length > 0 ? 'fuzzy' :
                            $(this).find('td:contains("Author+Year Match")').length > 0 ? 'author' :
                            $(this).find('td:contains("Reverse Fuzzy Match")').length > 0 ? 'reverse' : 'unmatched';
            $(this).addClass('match-' + matchType);
        });
    });
    </script>
    </body></html>
    """
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)


def main():
    start_time = time.time()
    
    # Initialize metadata index
    metadata_index = MetadataIndex()
    
    # Load BibTeX files
    for bib_file in CONFIG['bibtex_files']:
        if bib_file.exists():
            logger.info(f"Loading BibTeX file: {bib_file}")
            metadata_index.load_bibtex(bib_file)
        else:
            logger.error(f"BibTeX file not found: {bib_file}")
    
    # Load CSV files
    for csv_file in CONFIG['csv_files']:
        if csv_file.exists():
            logger.info(f"Loading CSV file: {csv_file}")
            metadata_index.load_csv(csv_file)
        else:
            logger.error(f"CSV file not found: {csv_file}")
    
    # Create output directory if it doesn't exist
    CONFIG['output_dir'].mkdir(parents=True, exist_ok=True)
    
    # Process PDFs
    processor = PDFProcessor(metadata_index)
    pdf_files = list(CONFIG['source_dir'].glob('*.pdf'))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONFIG['num_workers']) as executor:
        futures = [executor.submit(processor.process_pdf, pdf) for pdf in pdf_files]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                future.result()
                if (i + 1) % 10 == 0:
                    logger.info(f"Processed {i + 1}/{len(pdf_files)} PDFs...")
            except Exception as e:
                logger.error(f"Processing error: {e}")
    
    # Generate reports
    generate_reports(processor.results)
    
    # Log summary statistics
    match_types = defaultdict(int)
    for result in processor.results:
        match_types[result['match_type']] += 1
    
    logger.info("===== Matching Statistics =====")
    for match_type, count in match_types.items():
        logger.info(f"{match_type}: {count} files ({count/len(processor.results)*100:.1f}%)")
    
    logger.info(f"Processed {len(pdf_files)} PDFs in {time.time()-start_time:.2f} seconds")


if __name__ == "__main__":
    main()
