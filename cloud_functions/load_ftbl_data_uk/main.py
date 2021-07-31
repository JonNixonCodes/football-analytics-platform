# main.py

# %% Import external libraries
import os, sys
from flask import escape

# %% Import user libraries
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{root}/libraries")

# from football_analytics_platform.source.football_data_uk import get_csv_url, download_csv
# from football_analytics_platform.source.google_cloud_platform import set_google_application_credentials, upload_cloud_storage

# %% Define constants
LOCAL_TMP_DIR = "/tmp"
DESTINATION_BLOB_DIR = "landing/football-data-uk"

# %% Define functions
def get_json_value(request, key):
    """Get key,value from json flask.Request object
        Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
        key (str): The key to the key-value pair.
    Returns:
        The value corresponding to the key-value pair     
    """
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and key in request_json:
            value = request_json[key]
        else:
            raise ValueError(f"JSON is invalid, or missing a {key} property")
    else:
        raise ValueError("Unknown content type: {}".format(content_type))
    return value

def json_content(request):
    """ Responds to an HTTP request using data from the request body parsed
    according to the "content-type" header.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    name = get_json_value(request,"name")
    return 'Hello {}!'.format(escape(name))
    