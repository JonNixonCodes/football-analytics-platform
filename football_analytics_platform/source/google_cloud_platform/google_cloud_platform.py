# google_cloud_platform

# %% Import libraries
import os
from google.cloud import storage

# %% Define constants
GOOGLE_APPLICATION_CREDENTIALS_FILE_PATH = "/home/jon-dev/Workbench/Projects/football-analytics-platform/credentials/football-analytics-platform-fdf39ee7f4bb.json"

# %% Define functions
def set_google_application_credentials(credentials_file_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file_path

def upload_cloud_storage(bucket_name, destination_blob_path, source_file_path):
    """Upload file to Google Cloud Storage"""
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

def download_cloud_storage(destination_file_path, bucket_name, source_blob_path):
    """Download file from Google Cloud Storage"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_path)
    blob.download_to_filename(destination_file_path)
