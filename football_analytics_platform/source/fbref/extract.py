# fbref.extract.py

# %% Import libraries
import requests, re
from bs4 import BeautifulSoup

# %% Constants
BASE_URL = "https://fbref.com"
SEASONS_URL = "https://fbref.com/en/comps/"
COMPS_URL = "https://fbref.com/en/comps/"
TEAMS_URL = "https://fbref.com/en/squads/"

# %% Define functions
def extract_seasons():
    seasons = []
    r = requests.get(SEASONS_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    # winter seasons
    for a in soup.find_all(href=re.compile(r"/comps/season/\d{4}-\d{4}")):
        seasons.append(
            {
                'name':a.string,
                'link':BASE_URL + a['href']
            }
        )
    # summer season
    for a in soup.find_all(href=re.compile(r"/comps/season/\d{4}$")):
        seasons.append(
            {
                'name':" ".join(["summer",a.string]),
                'link':BASE_URL + a['href']
            }
        )
    return seasons

def extract_comps():
    comps = []
    r = requests.get(COMPS_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for table in soup.find_all("table"):
        tbody = table.find("tbody")
        for tr in tbody.find_all("tr"):
            comp_dict = {}
            for th in tr.find_all("th"):
                comp_dict.update({
                    th['data-stat']:th.string,
                    'link':BASE_URL + th.find("a")["href"]
                    })
            for td in tr.find_all("td"):
                comp_dict.update({td['data-stat']:td.string})
            comps.append(comp_dict)
    return comps

def extract_country_teams(url):
    teams = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for table in soup.find_all("table"):
        tbody = table.find("tbody")
        for tr in tbody.find_all("tr"):
            team_dict = {}
            for th in tr.find_all("th"):
                team_dict.update({
                    th['data-stat']:th.string,
                    'link':BASE_URL + th.find("a")["href"]
                    })
            for td in tr.find_all("td"):
                team_dict.update({td['data-stat']:td.string})
            teams.append(team_dict)
    return teams

def extract_teams():
    country_team_urls = []
    teams = []
    r = requests.get(TEAMS_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    for table in soup.find_all("table"):
        tbody = table.find("tbody")
        for tr in tbody.find_all("tr"):
            country_team_urls.append(
                BASE_URL + tr.find("th").find("a")["href"]
            )
    for url in country_team_urls:
        teams.extend(extract_country_teams(url))
    return teams
