# download_match_data.py

#%% Import libraries
import requests
import re
from bs4 import BeautifulSoup
from google.cloud import storage

#%% Define functions
def load_page(url):
    r = requests.get(url)
    return r.text

def extract_csv_urls(page, root_url):
    soup = BeautifulSoup(page,"html.parser")
    urls = [link.get("href") for link in soup.find_all("a")]
    csv_urls = [root_url + url for url in urls if re.match(r".*\.csv", url)!=None]
    return csv_urls

def extract_file_name(url):
    year = re.search(r"/(\d{4})/",url).group(1)
    comp_cd = re.search(r"/(\w+)\.csv",url).group(1)
    fname = year + "_" + comp_cd + ".csv"
    return fname

def download_file(url, file_name, out_dir_path):
    r = requests.get(url)
    out_file_path = out_dir_path + file_name
    open(out_file_path, 'wb').write(r.content)
