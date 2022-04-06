# football_data_uk.transform

# %% Import libraries
import csv, re
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
OUTPUT_COLUMNS = [
    {"name":"div", "source_name":"Div", "type":str, "default":None, "func":None},
    {"name":"seas", "source_name":None, "type":str, "default":None, "func":None},
    {"name":"date", "source_name":"Date", "type":str, "default":None, "func":date_string_conversion},
    {"name":"home_team", "source_name":"HomeTeam", "type":str, "default":None, "func":None},
    {"name":"away_team", "source_name":"AwayTeam", "type":str, "default":None, "func":None},
    {"name":"full_time_home_gls", "source_name":"FTHG", "type":int, "default":None, "func":None},
    {"name":"full_time_away_gls", "source_name":"FTAG", "type":int, "default":None, "func":None},
    {"name":"full_time_rslt", "source_name":"FTR", "type":str, "default":None, "func":None},
    {"name":"half_time_home_gls", "source_name":"HTHG", "type":str, "default":None, "func":None},
    {"name":"half_time_away_gls", "source_name":"HTAG", "type":str, "default":None, "func":None},
    {"name":"half_time_rslt", "source_name":"HTR", "type":str, "default":None, "func":None},
    {"name":"attn", "source_name":"Attendance", "type":str, "default":None, "func":None},
    {"name":"ref", "source_name":"Referee", "type":str, "default":None, "func":None},
    {"name":"home_team_shts", "source_name":"HS", "type":int, "default":None, "func":None},
    {"name":"away_team_shts", "source_name":"AS", "type":int, "default":None, "func":None},
    {"name":"home_shts_on_trgt", "source_name":"HST", "type":int, "default":None, "func":None},
    {"name":"away_shts_on_trgt", "source_name":"AST", "type":int, "default":None, "func":None},
    {"name":"home_team_hit_wood", "source_name":"HHW", "type":int, "default":None, "func":None},
    {"name":"away_team_hit_wood", "source_name":"AHW", "type":int, "default":None, "func":None},
    {"name":"home_team_crnr", "source_name":"HC", "type":int, "default":None, "func":None},
    {"name":"away_team_crnr", "source_name":"AC", "type":int, "default":None, "func":None},
    {"name":"home_team_foul", "source_name":"HF", "type":int, "default":None, "func":None},
    {"name":"away_team_foul", "source_name":"AF", "type":int, "default":None, "func":None},
    {"name":"home_team_offs", "source_name":"HO", "type":int, "default":None, "func":None},
    {"name":"away_team_offs", "source_name":"AO", "type":int, "default":None, "func":None},
    {"name":"home_team_yllw", "source_name":"HY", "type":int, "default":None, "func":None},
    {"name":"away_team_yllw", "source_name":"AY", "type":int, "default":None, "func":None},
    {"name":"home_team_red", "source_name":"HR", "type":int, "default":None, "func":None},
    {"name":"away_team_red", "source_name":"AR", "type":int, "default":None, "func":None}    
]

# %% Define functions
def extract_season_from_file_path(file_path):
    """Extract season from file path."""
    match = re.search(r"/(\d{4})_\w+.csv",file_path)
    if match == None:
        raise Exception("extract_season_from_file_path: No match found")
    return match.group(1)


def transform_csv_row(row, additional_fields={}):
    """Transform one row of data"""
    output_row = {}
    for col in OUTPUT_COLUMNS:
        source_key = col["source_name"]
        output_key = col["name"]
        output_val = col["default"]
        if source_key in row.keys():
            source_val = row[source_key]            
            output_key = col["name"]
            output_val = col["type"](source_val)
            if col["func"] != None:
                output_val = col["func"](output_val)
        output_row[output_key] = output_val
    output_row.update(additional_fields)
    return output_row


def is_row_empty(row):
    ret_val = False
    col = OUTPUT_COLUMNS[0]
    source_key = col["source_name"]
    if len(row[source_key])==0:
        ret_val = True
    return ret_val

def read_transform_csv_data(source_file_path):
    """Read source data and apply transformation"""
    data = []
    additional_fields = {"seas":extract_season_from_file_path(source_file_path)}
    with open(source_file_path, 'r', encoding='windows-1252') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if (is_row_empty(row) == True): # Skip empty rows
                continue
            tf_row = transform_csv_row(row, additional_fields)
            data.append(tf_row)
    return data


def write_data_to_file(destination_file_path, data):
    """Write data to destination"""
    with open(destination_file_path, 'w', newline='') as csv_file:
        fieldnames = [col["name"] for col in OUTPUT_COLUMNS]
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
