# test_transform_match_data_0.py

# %% Import libraries
import sys

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from src.transform_match_data import transform_csv

# %% Define constants
TEST_FILE_0 = "/home/jon-dev/Workbench/Projects/football-analytics-platform/data/landing/football-data-uk/0001_E0.csv"
TEST_FILE_1 = "/home/jon-dev/Workbench/Projects/football-analytics-platform/data/landing/football-data-uk/2021_E3.csv"

# %% Tests
def test_transform_csv_0():
    test_files = [TEST_FILE_0,TEST_FILE_1]
    for test in test_files:
        output_data = transform_csv(input_file_path=test)
        assert(len(output_data)) > 0
        assert(len(output_data[0])) > 0

# %% Main
def main():
    print("Running tests...")
    test_transform_csv_0()
    print("All passed!")

if __name__=="__main__":
    main()
