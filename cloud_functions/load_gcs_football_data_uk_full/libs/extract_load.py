# extract_load.py

# %% Import libraries
import requests, re
from bs4 import BeautifulSoup
from google.cloud import storage

# %% Define functions
def load_page(url):
    """Load web page. Return HTML."""
    r = requests.get(url)
    return r.text

def scrape_urls(html_text, pattern):
    """Extract URLs from raw html based on regex pattern"""
    soup = BeautifulSoup(html_text,"html.parser")
    anchors = soup.find_all("a")
    urls = [a.get("href") for a in anchors]
    return [url for url in urls if re.match(pattern, url)!=None]

def download_csv(destination_file_path, source_url):
    """Download CSV to destination file path from URL"""
    r = requests.get(source_url)
    if r.status_code!=200:
        raise Exception(f"GET request failed: {r.status_code}")
    open(destination_file_path, 'wb').write(r.content)

def upload_blob(bucket_name, destination_blob_path, source_file_path):
    """Upload blob to Google Cloud Storage"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_path)
    blob.upload_from_filename(source_file_path)
