# football_data_uk

 # %% Import libraries
import requests

# %% Constants
BASE_URL = "https://www.football-data.co.uk/mmz4281/SEASON/DIV.csv"

 # %% Define functions
def get_csv_url(season, division):
    """Get CSV URL"""
    csv_url = BASE_URL
    csv_url = csv_url.replace("SEASON",season)
    csv_url = csv_url.replace("DIV",division)
    return csv_url

def download_csv(output_path, csv_url):
    """Download CSV"""
    r = requests.get(csv_url)
    if r.status_code!=200:
        raise Exception(f"GET request failed: {r.status_code}")
    open(output_path, 'wb').write(r.content)

def upload_to_cloud_storage(bucket_name, destination_blob_path, input_path):
    """Download file and upload to Google Cloud Storage"""
    r = get_csv(season, division)
