# load_football_data_uk.py

# %% Import libraries
import sys

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from src.download_match_data import * 
from src.upload_cloud_storage import *

# %% Define constants
URL = "https://www.football-data.co.uk/englandm.php"
ROOT_URL = "https://www.football-data.co.uk/"
DEST_DIR = "/home/jon-dev/Workbench/Projects/football-analytics-platform/data/landing/football-data-uk/"
CRED_PATH = "/home/jon-dev/Workbench/Projects/football-analytics-platform/credentials/football-analytics-platform-fdf39ee7f4bb.json"
BUCKET_NAME = "football-analytics-platform"
BLOB_FOLDER = "landing/football-data-uk/"

#%% Main
def main():
    """ Load data from www.football-data.co.uk to Cloud Storage.
    
    Keyword arguments:
    bucket_name -- Cloud Storage bucket name
    """

    print("BEGIN")
    # Download data to local disk
    print("Starting download...")
    page = load_page(URL)
    urls = extract_csv_urls(page, ROOT_URL)
    #urls = urls[:1] # TESTING ONLY
    print(f"downloading {len(urls)} files to {DEST_DIR}")
    for url in urls:
        download_file(url, extract_file_name(url), DEST_DIR)
    print("Finished download!")
    # Upload data to cloud
    print("Starting upload...")
    set_google_application_credentials(CRED_PATH)
    files = os.listdir(DEST_DIR)
    print(f"Uploading {len(files)} files to {BUCKET_NAME}")
    for file in files:
        src_file_path = DEST_DIR + file
        dest_blob_path = extract_blob_path(BLOB_FOLDER, src_file_path)
        upload_cloud_storage(BUCKET_NAME, src_file_path, dest_blob_path)
    print("Finished upload!")
    print("END")

if __name__ == '__main__':
    main()