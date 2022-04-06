# test_football_data_uk_0.py

# %% Import libraries
import sys, os

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from football_analytics_platform.source.football_data_uk  import transform_csv

# %% Define constants
SEASON_0 = "0001"
SEASON_1 = "2021"
SEASON_2 = "1415"
SEASON_3 = "0405"
DIV_0 = "E0"
DIV_1 = "E3"
DIV_2 = "E0"
DIV_3 = "E0"
SRC_FILE_PATH_0 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_0}_{DIV_0}.csv"
SRC_FILE_PATH_1 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_1}_{DIV_1}.csv"
SRC_FILE_PATH_2 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_2}_{DIV_2}.csv"
SRC_FILE_PATH_3 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/{SEASON_3}_{DIV_3}.csv"
DEST_FILE_PATH_0 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/tf_{SEASON_0}_{DIV_0}.csv"
DEST_FILE_PATH_1 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/tf_{SEASON_1}_{DIV_1}.csv"
DEST_FILE_PATH_2 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/tf_{SEASON_2}_{DIV_2}.csv"
DEST_FILE_PATH_3 = f"/home/jon-dev/Workbench/Projects/football-analytics-platform/data/test/tf_{SEASON_3}_{DIV_3}.csv"

# %% Tests
def test_transform_csv_0():
    transform_csv(DEST_FILE_PATH_0, SRC_FILE_PATH_0)
    transform_csv(DEST_FILE_PATH_1, SRC_FILE_PATH_1)
    transform_csv(DEST_FILE_PATH_2, SRC_FILE_PATH_2)
    transform_csv(DEST_FILE_PATH_3, SRC_FILE_PATH_3)
    assert((os.path.exists(DEST_FILE_PATH_0)) and (os.path.getsize(DEST_FILE_PATH_0) > 0))
    assert((os.path.exists(DEST_FILE_PATH_1)) and (os.path.getsize(DEST_FILE_PATH_1) > 0))
    assert((os.path.exists(DEST_FILE_PATH_2)) and (os.path.getsize(DEST_FILE_PATH_2) > 0))
    assert((os.path.exists(DEST_FILE_PATH_3)) and (os.path.getsize(DEST_FILE_PATH_3) > 0))

# %% Main
def main():
    print("Running tests...")
    test_transform_csv_0()
    print("All passed!")

if __name__=="__main__":
    main()
