import sys
from typing import get_origin
from utils import get_project_root
from pathlib import Path

print(Path(__file__))
print(get_project_root())
print(get_project_root().joinpath("cloud_functions","load_gcs_football_data_uk_full","libs"))
sys.path.append(str(get_project_root().joinpath("cloud_functions","load_gcs_football_data_uk_full","libs")))
print(sys.path)