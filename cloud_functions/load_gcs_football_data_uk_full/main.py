# load_gcs_football_data_uk_full.main.py

# %% Import external libraries
import sys, click, yaml

# %% Import user libraries
from lib.football_data_uk import get_csv_url, download_csv
from lib.google_cloud_platform import set_google_application_credentials, upload_cloud_storage

# %% Define constants
ENGLAND_FOOTBALL_DATA_URL = "https://www.football-data.co.uk/englandm.php"
ROOT_URL = "https://www.football-data.co.uk/"
URL_PATTERN = r"mmz4281/\d{4}/\w{2}.csv"

#%% Define functions
@click.command()
@click.argument("config_path")
def run(config_path):
    """ Load data from www.football-data.co.uk to Cloud Storage"""
    print("BEGIN")

    # Read in yaml file
    with open(config_path, 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)

    # Download data to local disk
    print("Starting download...")
    for job in config["JOBS"]:
        source_url = get_csv_url(season=job["SEASON"], division=job["DIVISION"])
        download_csv(destination_file_path=job["LOCAL_PATH"], source_url=source_url)
    print("Finished download!")

    # Upload data to cloud
    print("Starting upload...")
    set_google_application_credentials(config["GOOGLE_CREDENTIAL_PATH"])
    for job in config["JOBS"]:
        upload_cloud_storage(
            bucket_name=config["BUCKET_NAME"], 
            destination_blob_path=job["DESTINATION_BLOB_PATH"], 
            source_file_path=job["LOCAL_PATH"])
    print("Finished upload!")

    print("END")

# %% Main
if __name__ == '__main__':
    run()