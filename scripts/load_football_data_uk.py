# load_football_data_uk.py

# %% Import libraries
from src.download_match_data import *
from src.upload_cloud_storage import *

#%% Main
def main():
    url = "https://www.football-data.co.uk/englandm.php"
    root_url = "https://www.football-data.co.uk/"
    # Create storage client
    client = storage.Client()
    # Create bucket object
    bucket = client.bucket("football-analytics-platform")
    # Create a blob
