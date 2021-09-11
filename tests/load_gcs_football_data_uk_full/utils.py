# utils.py

# %% Import external libraires
import os
from pathlib import Path

# %% Define functions
def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

def set_google_application_credentials(credentials_file_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file_path
