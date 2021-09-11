# load_gcs_football_data_uk_full.main.py

# %% Import external libraries
import re, os, tempfile

# %% Import user libraries
from libs.extract_load import load_page, scrape_urls, download_csv, upload_blob

# %% Define constants
FOOTBALL_DATA_URL = "https://www.football-data.co.uk/englandm.php"
ROOT_URL = "https://www.football-data.co.uk/"
URL_REGEX_PATTERN = r"mmz4281/\d{4}/\w{2}.csv"
SEASON_REGEX_PATTERN = r".*mmz4281/(\d{4})/\w{2}.csv"
COMPETITION_REGEX_PATTERN = r".*mmz4281/\d{4}/(\w{2}).csv"
BUCKET_NAME = "football-analytics-platform"
BLOB_DIR = "landing/football-data-uk"
TMP_DIR = tempfile.gettempdir()

#%% Define functions
def format_url(relative_url, root_url=ROOT_URL):
    return root_url+relative_url

def name_file(url):
    season_match = re.match(SEASON_REGEX_PATTERN, url)
    competition_match = re.match(COMPETITION_REGEX_PATTERN, url)
    if season_match and competition_match:
        season = str(season_match.group(1))
        competition = str(competition_match.group(1))
    else:
        return None
    return f"{season}_{competition}.csv"

def extract_load_one_file(bucket_name, tmp_dir, blob_dir, source_url):
    filename = name_file(source_url)
    tmp_file_path = tmp_dir+"/"+filename
    blob_path = blob_dir+"/"+filename
    download_csv(\
        destination_file_path=tmp_file_path, 
        source_url=source_url)
    upload_blob(\
        bucket_name=bucket_name, 
        destination_blob_path=blob_path, 
        source_file_path=tmp_file_path)
    # Delete temporary file
    # os.remove(tmp_file_path)

def run():
    """ Full batch load of data from www.football-data.co.uk to Cloud Storage"""
    # Load page
    html_text = load_page(FOOTBALL_DATA_URL)
    # Extract list of URLs to downloadable CSV files
    urls = scrape_urls(html_text=html_text, pattern=URL_REGEX_PATTERN)
    urls = [url for url in map(lambda x: format_url(relative_url=x), urls)]
    # TEST
    urls = urls[:10]
    # Extract and Load each CSV file
    map(\
        lambda x: extract_load_one_file(\
            bucket_name=BUCKET_NAME, 
            tmp_dir=TMP_DIR,
            blob_dir=BLOB_DIR,
            source_url=x),
        urls)

# %%
