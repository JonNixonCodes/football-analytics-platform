# football_data_uk.transform

# %% Import libraries
import csv
from datetime import datetime

# %% Define column functions
def date_string_conversion(in_date_str):
    """Convert date from d/m/y to Y-m-d"""
    if len(in_date_str)==10: # date string format: "%d/%m/%Y"
        in_date_dt = datetime.strptime(in_date_str, "%d/%m/%Y")
    elif len(in_date_str)==8: # date string format: "%d/%m/%y"
        in_date_dt = datetime.strptime(in_date_str, "%d/%m/%y")
    else:
        raise("Invalid date string")
    out_date_str = datetime.strftime(in_date_dt, "%Y-%m-%d")
    return out_date_str

# %% Define column mapping
COLUMN_MAP = {
    "Div":{"name":"div", "type":str, "default":None, "func":None},
    "Date":{"name":"date", "type":str, "default":None, "func":date_string_conversion},
    "HomeTeam":{"name":"home_team", "type":str, "default":None, "func":None},
    "AwayTeam":{"name":"away_team", "type":str, "default":None, "func":None},
    "FTHG":{"name":"full_time_home_gls", "type":int, "default":None, "func":None},
    "FTAG":{"name":"full_time_away_gls", "type":int, "default":None, "func":None},
    "FTR":{"name":"full_time_rslt", "type":str, "default":None, "func":None},
    "HTHG":{"name":"half_time_home_gls", "type":str, "default":None, "func":None},
    "HTAG":{"name":"half_time_away_gls", "type":str, "default":None, "func":None},
    "HTR":{"name":"half_time_rslt", "type":str, "default":None, "func":None},
    "Attendance":{"name":"attn", "type":str, "default":None, "func":None},
    "Referee":{"name":"ref", "type":str, "default":None, "func":None},
    "HS":{"name":"home_team_shts", "type":int, "default":None, "func":None},
    "AS":{"name":"away_team_shts", "type":int, "default":None, "func":None},
    "HST":{"name":"home_shts_on_trgt", "type":int, "default":None, "func":None},
    "AST":{"name":"away_shts_on_trgt", "type":int, "default":None, "func":None},
    "HHW":{"name":"home_team_hit_wood", "type":int, "default":None, "func":None},
    "AHW":{"name":"away_team_hit_wood", "type":int, "default":None, "func":None},
    "HC":{"name":"home_team_crnr", "type":int, "default":None, "func":None},
    "AC":{"name":"away_team_crnr", "type":int, "default":None, "func":None},
    "HF":{"name":"home_team_foul", "type":int, "default":None, "func":None},
    "AF":{"name":"away_team_foul", "type":int, "default":None, "func":None},
    "HO":{"name":"home_team_offs", "type":int, "default":None, "func":None},
    "AO":{"name":"away_team_offs", "type":int, "default":None, "func":None},
    "HY":{"name":"home_team_yllw", "type":int, "default":None, "func":None},
    "AY":{"name":"away_team_yllw", "type":int, "default":None, "func":None},
    "HR":{"name":"home_team_red", "type":int, "default":None, "func":None},
    "AR":{"name":"away_team_red", "type":int, "default":None, "func":None}
}

# %% Define functions
def transform_csv_row(row):
    """Transform one row of data"""
    output_row = {}
    for k in COLUMN_MAP.keys():
        if k in row.keys():
            output_key = COLUMN_MAP[k]["name"]
            output_val = COLUMN_MAP[k]["type"](row[k])
            if COLUMN_MAP[k]["func"] != None:
                output_val = COLUMN_MAP[k]["func"](row[k])          
        else:
            output_key = COLUMN_MAP[k]["name"]
            output_val = COLUMN_MAP[k]["default"]
        output_row[output_key] = output_val
    return output_row

def read_transform_csv_data(source_file_path):
    """Read source data and apply transformation"""
    data = []
    with open(source_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            tf_row = transform_csv_row(row)
            data.append(tf_row)
    return data

def write_data_to_file(destination_file_path, data):
    """Write data to destination"""
    with open(destination_file_path, 'w', newline='') as csv_file:
        fieldnames = [v["name"] for v in COLUMN_MAP.values()]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def transform_csv(destination_file_path, source_file_path):
    """Transform CSV file from football-data.uk"""
    # Read source data and apply transformations
    output_data = read_transform_csv_data(source_file_path)
    # Write transformed data to destination file path
    write_data_to_file(destination_file_path, output_data)


