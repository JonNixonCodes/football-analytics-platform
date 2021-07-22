# landing_to_staging.py

# %% Import external libraries
import sys, click, yaml

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from football_analytics_platform.source.football_data_uk import transform_csv
from football_analytics_platform.source.google_cloud_platform import set_google_application_credentials, upload_cloud_storage, download_cloud_storage

#%% Define functions
@click.command()
@click.argument("config_path")
def run(config_path):
    """ Download data from landing directory. Apply transformations. Upload data to staging directory in Cloud Storage"""
    print("BEGIN")

    # Read in yaml file
    with open(config_path, 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)

    set_google_application_credentials(config["GOOGLE_CREDENTIAL_PATH"])

    print("Starting jobs...")
    for job in config["JOBS"]:
        download_cloud_storage(job["LOCAL_TEMP_PATH"],config["BUCKET_NAME"],job["SOURCE_BLOB_PATH"])
        transform_csv(job["LOCAL_STAGING_PATH"],job["LOCAL_TEMP_PATH"])
        upload_cloud_storage(config["BUCKET_NAME"],job["DESTINATION_BLOB_PATH"],job["LOCAL_STAGING_PATH"])
    print("Finished jobs!")

    print("END")

# %% Main
if __name__ == '__main__':
    run()