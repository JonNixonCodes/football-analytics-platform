# download_match_data.py

#%% Import libraries
import requests
import re
from bs4 import BeautifulSoup
from google.cloud import storage

#%% Define functions
def load_page(url):
    """Load web page."""
    r = requests.get(url)
    return r.text

def extract_csv_urls(page, root_url):
    """Extract urls for downloading csv files and append a root url.

    Keyword arguments:
    page -- Webpage as a raw HTML
    root_url -- URL to append to output url
    """
    soup = BeautifulSoup(page,"html.parser")
    urls = [link.get("href") for link in soup.find_all("a")]
    csv_urls = [root_url + url for url in urls if re.match(r".*\.csv", url)!=None]
    return csv_urls

def extract_file_name(url):
    """Extract filename from url."""
    year = re.search(r"/(\d{4})/",url).group(1)
    comp_cd = re.search(r"/(\w+)\.csv",url).group(1)
    fname = year + "_" + comp_cd + ".csv"
    return fname

def download_file(url, file_name, dest_dir_path):
    """Download file from url to output directory.

    Keyword arguments:
    url -- URL of file to download
    file_name -- File name
    dest_dir_path -- Destination directory path
    """
    r = requests.get(url)
    out_file_path = dest_dir_path + file_name
    open(out_file_path, 'wb').write(r.content)
