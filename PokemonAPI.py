import requests
import json
import pandas as pd

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

#a = get_by_ability('torrent')
#a_list = get_pokes_from_json(a)
#for pokes in a_list:
  #print(pokes)

t = get_by_type('fire')
t_list = get_pokes_from_json(t)

t2 = get_by_type('flying')
t2_list = get_pokes_from_json(t2)

print(compare_poke_lists(t_list, t2_list))


#blah