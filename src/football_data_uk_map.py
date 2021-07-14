# %% Import libraries
from datetime import datetime

# %% Define functions
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
    "Div":{"name":"div", "type":str, "func":None},
    "Date":{"name":"date", "type":str, "func":date_string_conversion},
    "HomeTeam":{"name":"home_team", "type":str, "func":None},
    "AwayTeam":{"name":"away_team", "type":str, "func":None},
    "FTHG":{"name":"full_time_home_gls", "type":int, "func":None},
    "FTAG":{"name":"full_time_away_gls", "type":int, "func":None},
    "FTR":{"name":"full_time_rslt", "type":str, "func":None},
    "HTHG":{"name":"half_time_home_gls", "type":str, "func":None},
    "HTAG":{"name":"half_time_away_gls", "type":str, "func":None},
    "HTR":{"name":"half_time_rslt", "type":str, "func":None},
    "Attendance":{"name":"attn", "type":str, "func":None},
    "Referee":{"name":"ref", "type":str, "func":None},
    "HS":{"name":"home_team_shts", "type":int, "func":None},
    "AS":{"name":"away_team_shts", "type":int, "func":None},
    "HST":{"name":"home_shts_on_trgt", "type":int, "func":None},
    "AST":{"name":"away_shts_on_trgt", "type":int, "func":None},
    "HHW":{"name":"home_team_hit_wood", "type":int, "func":None},
    "AHW":{"name":"away_team_hit_wood", "type":int, "func":None},
    "HC":{"name":"home_team_crnr", "type":int, "func":None},
    "AC":{"name":"away_team_crnr", "type":int, "func":None},
    "HF":{"name":"home_team_foul", "type":int, "func":None},
    "AF":{"name":"away_team_foul", "type":int, "func":None},
    "HO":{"name":"home_team_offs", "type":int, "func":None},
    "AO":{"name":"away_team_offs", "type":int, "func":None},
    "HY":{"name":"home_team_yllw", "type":int, "func":None},
    "AY":{"name":"away_team_yllw", "type":int, "func":None},
    "HR":{"name":"home_team_red", "type":int, "func":None},
    "AR":{"name":"away_team_red", "type":int, "func":None}
}