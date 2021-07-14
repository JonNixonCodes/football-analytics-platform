# transform_match_data.py

# %% Import libraries
import sys, csv
from datetime import datetime

# %% Import user libraries
sys.path.append("/home/jon-dev/Workbench/Projects/football-analytics-platform")

from src.football_data_uk_map import COLUMN_MAP

# %% Define functions
def transform_csv(input_file_path):
    """Transform data from football-data.uk"""
    output_data = []
    with open(input_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            output_row = {}
            for k,v in row.items():
                if k in COLUMN_MAP.keys():
                    output_key = COLUMN_MAP[k]["name"]
                    output_val = COLUMN_MAP[k]["type"](v)
                    if COLUMN_MAP[k]["func"] != None:
                        output_val = COLUMN_MAP[k]["func"](v)
                    output_row[output_key] = output_val
            output_data.append(output_row)
    return output_data



