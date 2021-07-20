# test_google_cloud_platform_0.py

# %% Import external libraries
import sys, os
from google.cloud import storage

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from football_analytics_platform.source.google_cloud_platform import set_google_application_credentials, upload_cloud_storage

# %% Define constants
SEASON_0 = "9900"
SEASON_1 = "2021"
DIV_0 = "E0"
DIV_1 = "EC"
GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH = "/home/jon-dev/Workbench/Projects/football-analytics-platform/.credentials/football-analytics-platform-fdf39ee7f4bb.json"
BUCKET_NAME = "football-analytics-platform"
DEST_BLOB_PATH_0 = f"test/{SEASON_0}_{DIV_0}.csv"
DEST_BLOB_PATH_1 = f"test/{SEASON_1}_{DIV_1}.csv"
SRC_FILE_PATH_0 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_0}_{DIV_0}.csv"
SRC_FILE_PATH_1 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_1}_{DIV_1}.csv"

# %% Tests
def test_set_google_application_credentials_0():
    set_google_application_credentials(GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH)
    assert(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') != None)

def test_upload_cloud_storage_0():
    # Setup Cloud Storage client
    set_google_application_credentials(GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH)
    storage_client = storage.Client()
    # Upload test files to cloud storage
    upload_cloud_storage(BUCKET_NAME, DEST_BLOB_PATH_0, source_file_path=SRC_FILE_PATH_0)
    upload_cloud_storage(BUCKET_NAME, DEST_BLOB_PATH_1, source_file_path=SRC_FILE_PATH_1)
    # Check files are in cloud storage
    blob_names = [b.name for b in storage_client.list_blobs(BUCKET_NAME)]
    assert(DEST_BLOB_PATH_0 in blob_names)
    assert(DEST_BLOB_PATH_1 in blob_names)

# %% Main
def main():
    print("Running tests...")
    test_set_google_application_credentials_0()
    test_upload_cloud_storage_0()
    print("All passed!")

if __name__=="__main__":
    main()
