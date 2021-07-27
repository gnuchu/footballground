import json

config_file = "postcodes.json"

with open(config_file, "r") as f:
  data = json.loads(f.read())

strip_space = lambda x: x.replace(" ", "")

home = strip_space(data['home'])
away = list(map(strip_space, data['away']))

for destination in away:
  