import yaml
import requests
import sys
import json
from datetime import date, datetime

def get_config(path):
  with open(path, 'r') as stream:
    try:
      config = yaml.load(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
      print(exc)
  
  return config

def format_date(ds):
  d = datetime.fromisoformat(ds)
  f = "%Y-%m-%d %H:%M:%S"

  str = d.strftime(f)
  return str

config_file='./conf/api.yaml'
config=get_config(config_file)

season = config['season']
leagues = config['leagues']
country = config['country']
api_key = config['api_key']
api_host = config['api_host']
url = config['fixtures_url']

headers = {
  'x-rapidapi-key': f"{api_key}",
  'x-rapidapi-host': f"{api_host}"
}


for league in leagues:
  querystring = {
    "league": f"{league['id']}",
    "season": f"{season}"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  j = json.loads(response.text)
  
  outputfile = f"output/{league['name']}_fixtures_{season}.csv"
  f = open(outputfile, "w")

  for item in j['response']:
    fixture = item['fixture']
    league = item['league']
    teams = item['teams']
    date =format_date(fixture['date'])

    f.write(f"{teams['home']['name']},{teams['away']['name']},{league['name']},{fixture['venue']['name']},{date}\n")
  f.close()
