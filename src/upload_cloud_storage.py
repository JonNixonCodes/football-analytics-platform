# upload_cloud_storage.py

# %% Import libraries
import os
from google.cloud import storage

# %% Define functions
def set_google_application_credentials(credentials_file_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file_path

def upload_cloud_storage(bucket_name, source_file_path, destination_blob_path):
    """Uploads a file to Cloud Storage bucket."""
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
