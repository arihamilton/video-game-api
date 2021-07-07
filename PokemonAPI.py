import requests
import requests_cache
import json
import pandas as pd
import plotly.graph_objects as go

#response = requests.get("https://api.open-notify.org/astros.json")
#https://pokeapi.co/api/v2/ability/{insert pokemon name/id}
# 1. Connect to the Pokemon API
# 2. Create a function to get a list of pokemon with a specific type

# Test 1: Lowercase input
# Test 2: Uppercase input
# Test 3: Invalid input
def get_by_type(type_name):
  type_name = type_name.lower()
  r = requests.get('https://pokeapi.co/api/v2/type/' + str(type_name) + '/')
  response_code = r.status_code
  #print(response_code)
  if response_code == 200:
    return r
  return -1


# 3. Create a function to get a list of pokemon by gender

# Test 1: Lowercase input
# Test 2: Uppercase input
# Test 3: Invalid input
def get_by_gender(gender_name):
  gender_name = gender_name.lower()
  r = requests.get('https://pokeapi.co/api/v2/gender/' + str(gender_name) + '/')
  response_code = r.status_code
  #print(response_code)
  if response_code == 200:
    return r
  return -1

# 4. Create a function to get a list of pokemon by their abilities

# Test 1: Lowercase input
# Test 2: Uppercase input
# Test 3: Invalid input
def get_by_ability(ability_name):
  ability_name = ability_name.lower()
  r = requests.get('https://pokeapi.co/api/v2/ability/' + str(ability_name) + '/')
  response_code = r.status_code
  #print(response_code)
  if response_code == 200:
    return r
  return -1

# 5. Create a function to get a list of pokemon by their moveset

def get_pokes_from_json(r):
  pokemon_list = []
  try: 
    dict = r.json()
    if 'pokemon' in dict:
      list = dict['pokemon']
      for pokes in list:
        pokemon_list.append(pokes['pokemon'])
  except:
    print("no pokemon in list")
  finally:
    return pokemon_list

# 6. Let the user use the above functions to generate a team and put this information into a new table

def compare_poke_lists(list_1, list_2):
  complete_list = []
  for pokemon in list_1:
    if pokemon in list_2:
      complete_list.append(pokemon)
  return complete_list

def valid_type_input(type):
  if type in TYPES:
    return True
  return False

def generate_suggestion(str, list):
  for item in list:
    if str in item:
      response = input("Did you mean " + item + "? (yes/no) ")
      if response == 'yes':
        return item
  return -1
      
def get_user_input():
    valid = False
    type_1 = ""
    type_2 = ""
    valid_type1 = False
    valid_type2 = False
    while not valid:
      while not valid_type1:
          type_1 = input("Enter Type 1: ")
          if valid_type_input(type_1):
              valid_type1 = True
          else:
              print("Invalid input.")
              suggestion = generate_suggestion(type_1, TYPES)
              if suggestion != -1:
                  type_1 = suggestion
                  valid_type1 = True
      
      while not valid_type2:
          type_2 = input("Enter Type 2: ")
          if valid_type_input(type_2):
              valid_type2 = True
              valid = True
          else:
              print("Invalid input.")
              suggestion = generate_suggestion(type_2, TYPES)
              if suggestion != -1:
                  type_2 = suggestion
                  valid_type2 = True
                  valid = True
  
    return [type_1, type_2]
  
def get_pokemon_in_list(list):
  poke_list = []
  for pokemon in list:
    url = pokemon['url']
    r = requests.get(url)
    response_code = r.status_code
    if response_code == 200:
        dict = r.json()
        poke_id = dict['id']
        poke_name = dict['name']
        sprite = dict['sprites']['front_default']
        stats = []
        stat_dict = dict['stats']
        for item in stat_dict:
          stat_name = item['stat']['name']
          stat_value = item['base_stat']
          stats.append([stat_name, stat_value])

    poke_list.append([poke_id, poke_name, sprite, stats])
    
  return poke_list
    
#a = get_by_ability('torrent')
#a_list = get_pokes_from_json(a)
#for pokes in a_list:
  #print(pokes)
  
TYPES = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dark', 'dragon', 'steel', 'fairy']

#requests_cache.install_cache('pokemon_cache', backend='sqlite', expire_after=3600)

user_input = get_user_input()
print(user_input)
t = get_by_type(user_input[0])
t_list = get_pokes_from_json(t)

t2 = get_by_type(user_input[1])
t2_list = get_pokes_from_json(t2)

combination = compare_poke_lists(t_list, t2_list)

pokes = get_pokemon_in_list(combination)
for pokemon in pokes:
  print(pokemon)

##################### Figure creation, tidy up code later #####################

poke = pokes[0]
fig = go.Figure()

stats = poke[3]
x = []
y = []
for items in stats:
  x.append(items[0])
  y.append(items[1])

colors = ['crimson', 'coral', 'moccasin', 'lightskyblue', 'lightgreen', 'lightpink']  
  
fig.add_trace(go.Bar(x=x, y=y, marker_color=colors))

# Add image
img = poke[2]
fig.add_layout_image(
    dict(
        source=img,
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

name = poke[1]
# Update layout
fig.update_layout(title=(name))
fig.write_html('' + name + '.html') # export to HTML file


#blah