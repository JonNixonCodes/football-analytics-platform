# test_extract_load_0.py

# %% Import libraries
import sys,os
from google.cloud import storage

# %% Import user libraries
from utils import get_project_root, set_google_application_credentials
sys.path.append(str(get_project_root().joinpath("cloud_functions","load_gcs_football_data_uk_full")))
from libs.extract_load import load_page, scrape_urls, download_csv, upload_blob

# %% Define constants
GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH = "C:\\Users\\Jon Nixon\\Workbench\Projects\\football-analytics-platform\\.credentials\\football-analytics-platform-675fac055f68.json"
TEST_URL_0 = "https://www.football-data.co.uk/englandm.php"
TEST_PATTERN_0 = r"mmz4281/\d{4}/\w{2}.csv"
TEST_TMP_DIR = str(get_project_root().joinpath("tests","tmp"))
SEASON_0 = "9900"
SEASON_1 = "2021"
DIV_0 = "E0"
DIV_1 = "EC"
TEST_DEST_FILE_0 = TEST_TMP_DIR + f"/{SEASON_0}_{DIV_0}.csv"
TEST_DEST_FILE_1 = TEST_TMP_DIR + f"/{SEASON_1}_{DIV_1}.csv"
SOURCE_URL_0 = f"https://www.football-data.co.uk/mmz4281/{SEASON_0}/{DIV_0}.csv"
SOURCE_URL_1 = f"https://www.football-data.co.uk/mmz4281/{SEASON_1}/{DIV_1}.csv"
TEST_BUCKET_NAME = "football-analytics-platform"
TEST_BLOB_PATH_0 = f"test/{SEASON_0}_{DIV_0}.csv"
TEST_BLOB_PATH_1 = f"test/{SEASON_1}_{DIV_1}.csv"

# %% Tests
def test_load_page_0():
    assert(len(load_page(url=TEST_URL_0)) > 0)

def test_scrape_urls_0():
    html_text = load_page(url=TEST_URL_0)
    assert(len(scrape_urls(html_text=html_text, pattern=TEST_PATTERN_0)) > 0)

def test_download_csv_0():
    download_csv(destination_file_path=TEST_DEST_FILE_0, source_url=SOURCE_URL_0)
    download_csv(destination_file_path=TEST_DEST_FILE_1, source_url=SOURCE_URL_1)
    assert((os.path.exists(TEST_DEST_FILE_0)) and (os.path.getsize(TEST_DEST_FILE_0) > 0))
    assert((os.path.exists(TEST_DEST_FILE_1)) and (os.path.getsize(TEST_DEST_FILE_1) > 0))
    # clean-up test files
    os.remove(TEST_DEST_FILE_0)
    os.remove(TEST_DEST_FILE_1)

def test_upload_blob_0():
    # Setup Cloud Storage client
    set_google_application_credentials(GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH)
    storage_client = storage.Client()
    # Download test files
    download_csv(destination_file_path=TEST_DEST_FILE_0, source_url=SOURCE_URL_0)
    download_csv(destination_file_path=TEST_DEST_FILE_1, source_url=SOURCE_URL_1)
    # Check that files were downloaded
    assert((os.path.exists(TEST_DEST_FILE_0)) and (os.path.getsize(TEST_DEST_FILE_0) > 0))
    assert((os.path.exists(TEST_DEST_FILE_1)) and (os.path.getsize(TEST_DEST_FILE_1) > 0))
    # Upload test files to cloud storage
    upload_blob(bucket_name=TEST_BUCKET_NAME, destination_blob_path=TEST_BLOB_PATH_0, source_file_path=TEST_DEST_FILE_0)
    upload_blob(bucket_name=TEST_BUCKET_NAME, destination_blob_path=TEST_BLOB_PATH_1, source_file_path=TEST_DEST_FILE_1)
    # Check files are in cloud storage
    blob_names = [b.name for b in storage_client.list_blobs(TEST_BUCKET_NAME)]
    assert(TEST_BLOB_PATH_0 in blob_names)
    assert(TEST_BLOB_PATH_1 in blob_names)
    # Clean-up test files
    storage_client.bucket(TEST_BUCKET_NAME).blob(TEST_BLOB_PATH_0).delete()
    storage_client.bucket(TEST_BUCKET_NAME).blob(TEST_BLOB_PATH_1).delete()
    os.remove(TEST_DEST_FILE_0)
    os.remove(TEST_DEST_FILE_1)

# %% Main
def main():
    print("Running tests...")
    test_load_page_0()
    test_scrape_urls_0()
    test_download_csv_0()
    test_upload_blob_0()
    print("All passed!")

if __name__=="__main__":
    main()
