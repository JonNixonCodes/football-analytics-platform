# football_data_uk

# %% Import libraries
import requests
from google.cloud import storage

# %% Constants
BASE_URL = "https://www.football-data.co.uk/mmz4281/SEASON/DIV.csv"

# %% Define functions
def get_csv_url(season, division):
    """Get CSV URL"""
    csv_url = BASE_URL
    csv_url = csv_url.replace("SEASON",season)
    csv_url = csv_url.replace("DIV",division)
    return csv_url

def download_csv(destination_file_path, source_url):
    """Download CSV"""
    r = requests.get(source_url)
    if r.status_code!=200:
        raise Exception(f"GET request failed: {r.status_code}")
    open(destination_file_path, 'wb').write(r.content)
