# test_football_data_uk_0.py

# %% Import libraries
import sys,os

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from football_analytics_platform.src.football_data_uk import get_csv_url, download_csv

# %% Define constants
SEASON_0 = "9900"
SEASON_1 = "2021"
DIV_0 = "E0"
DIV_1 = "EC"
SOURCE_URL_0 = f"https://www.football-data.co.uk/mmz4281/{SEASON_0}/{DIV_0}.csv"
SOURCE_URL_1 = f"https://www.football-data.co.uk/mmz4281/{SEASON_1}/{DIV_1}.csv"
DESTINATION_FILE_PATH_0 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_0}_{DIV_0}.csv"
DESTINATION_FILE_PATH_1 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_1}_{DIV_1}.csv"

# %% Tests
def test_get_csv_url_0():
    assert(get_csv_url(SEASON_0, DIV_0) == SOURCE_URL_0)
    assert(get_csv_url(SEASON_1, DIV_1) == SOURCE_URL_1)

def test_download_csv_0():
    csv_url_0 = get_csv_url(SEASON_0, DIV_0)
    csv_url_1 = get_csv_url(SEASON_1, DIV_1)
    download_csv(DESTINATION_FILE_PATH_0, csv_url_0)
    download_csv(DESTINATION_FILE_PATH_1, csv_url_1)
    assert((os.path.exists(DESTINATION_FILE_PATH_0)) and (os.path.getsize(DESTINATION_FILE_PATH_0) > 0))
    assert((os.path.exists(DESTINATION_FILE_PATH_1)) and (os.path.getsize(DESTINATION_FILE_PATH_1) > 0))

# %% Main
def main():
    print("Running tests...")
    test_get_csv_url_0()
    test_download_csv_0()
    print("All passed!")

if __name__=="__main__":
    main()
