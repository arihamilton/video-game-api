import requests
import json
import pandas as pd

#response = requests.get("https://api.open-notify.org/astros.json")
#https://pokeapi.co/api/v2/ability/{insert pokemon name/id}
# 1. Connect to the Pokemon API
# 2. Create a function to get a list of pokemon with a specific type
# 3. Create a function to get a list of pokemon by gender
# 4. Create a function to get a list of pokemon by their abilities

# Test 1: Lowercase input
def get_by_ability(ability_name):
  r = requests.get('https://pokeapi.co/api/v2/ability/' + str(ability_name) + '/')
  response_code = str(r)
  r_dict = r.json()
  print(r_dict)

# 5. Create a function to get a list of pokemon by their moveset
# 6. Let the user use the above functions to generate a team and put this information into a new table

get_by_ability('torrent')
