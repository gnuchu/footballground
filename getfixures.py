import yaml
import requests
import sys
import json

def get_config(path):
  with open(path, 'r') as stream:
    try:
      config = yaml.load(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
      print(exc)
  
  return config


config_file='./api.yaml'
config=get_config(config_file)

season = config['season']
leagues = config['leagues']
country = config['country']

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
api_key = "FsCmAMgX9wmshWzee5mkjIKYDNGup1uXi63jsnaZYcBBNBAg4L"
api_host = "api-football-v1.p.rapidapi.com"
headers = {
  'x-rapidapi-key': f"{api_key}",
  'x-rapidapi-host': f"{api_host}"
}

c = 0


with open("fixtures.csv", "w") as f:
  for league in leagues:
    querystring = {
      "league": f"{league['id']}",
      "season": f"{season}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    j = json.loads(response.text)
    
    for item in j['response']:
      c += 1
      fixture = item['fixture']
      league = item['league']
      teams = item['teams']

      f.write(f"{teams['home']['name']},{teams['away']['name']},{league['name']},{fixture['venue']['name']},{fixture['date']}\n")
