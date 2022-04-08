# Global (instance-wide) scope
# This computation runs at instance cold-start

# Import libraries
import requests
import tempfile
import datetime
import yaml
from google.cloud import storage

# Set up Google Cloud Storage
bucket_name = "football-analytics-platform"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

# Load config file
config_blob_name = "config/football_data_uk_test.yml"
config_blob = bucket.blob(config_blob_name)
contents = config_blob.download_as_string()
config = yaml.safe_load(contents)

# Set up project parameters
project_id = config['PROJECT_ID']
destination_blob_dir = config['DESTINATION_BLOB_DIR']
bucket_name = config['BUCKET_NAME']

def run(request):
    # Per-function scope
    # This computation runs every time this function is called

    # Iterate through each job in the config file
    for j in config['JOBS']:
        # Set up job parameters
        source_url = j["SOURCE_URL"]
        output_file_prefix = j["OUTPUT_FILE_PREFIX"]
        output_file_name = output_file_prefix+"_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".csv"
        temp_file_path = tempfile.gettempdir()+"/"+output_file_name
        destination_blob_path = destination_blob_dir+"/"+output_file_name
        # Set up Google Cloud Storage objects
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_path)
        # Download CSV file to temporary location
        r = requests.get(source_url)
        if r.status_code!=200:
            raise Exception(f"GET request failed: {r.status_code}")
        open(temp_file_path, 'wb').write(r.content)
        # Write temporary file to Google Cloud Storage
        blob.upload_from_filename(temp_file_path)
        return 'OK'
