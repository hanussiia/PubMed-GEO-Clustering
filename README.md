# PubMed to GEO Dataset Clustering Tool

A Streamlit web application that clusters GEO datasets associated with PubMed articles based on their textual similarity using TF-IDF and K-Means clustering.

## Features

- Upload a file with PubMed IDs (PMIDs) to analyze
- Automatically retrieves associated GEO datasets from NCBI
- Processes dataset metadata (Title, Summary, Organism, Type, Overall Design)
- Creates TF-IDF vector representations
- Computes cosine similarity between datasets
- Determines optimal number of clusters using the elbow method
- Visualizes clusters and similarity matrices

## Requirements

- Python 3.7+
- Required Python packages:
  - streamlit
  - requests
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - numpy

## Installation

1. Clone the repository (if available) or create a directory with these files:
   - `extract.py` 
   - `clustering.py` 
   - `app.py`

2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

3. Install packages::
   ```bash
   pip3 install -r requirements.txt
## Usage

1. Prepare text file with one PMID per line (e.g., pmids.txt):
   `25404168
    12345678
    87654321`

2. Run application:
   ```bash
   streamlit run app.py
3. Upload file via web interface
