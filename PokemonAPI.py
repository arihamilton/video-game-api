import requests
import json
import os
import pandas as pd
import plotly.graph_objects as go
from DatabaseManagement import *

# response = requests.get("https://api.open-notify.org/astros.json")
# https://pokeapi.co/api/v2/ability/{insert pokemon name/id}
# 1. Connect to the Pokemon API
# 2. Create a function to get a list of pokemon with a specific type

# Test 1: Lowercase input
# Test 2: Uppercase input
# Test 3: Invalid input
# Test 4: Empty input
def get_by_type(type_name):
    if type_name == '':
      return -1
    type_name = type_name.lower()
    r = requests.get('https://pokeapi.co/api/v2/type/' + str(type_name) + '/')
    response_code = r.status_code
    # print(response_code)
    if response_code == 200:
        return r
    return -1


# 5. Create a function to get a list of pokemon by their moveset

# Test 1: Valid request
# Test 2: Invalid request
# Test 3: Empty request
def get_pokes_from_json(r):
    pokemon_list = []
    try: 
      dict = r.json()
      if 'pokemon' in dict:
        list = dict['pokemon']
        for pokes in list:
          if not 'gmax' in str(pokes['pokemon']['name']):
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


# Test 1: Lowercase input
# Test 2: Uppercase input
# Test 3: Invalid input
def valid_type_input(type):
    type = type.lower()
    if type in TYPES:
        return True
    return False


def generate_suggestion(str, list):
    if str == '':
        return -1
    for item in list:
        if str in item:
            response = input("Did you mean " + item + "? (yes/no) ")
            if response == 'yes':
                return item
    return -1


def get_team_inputs():
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
            if type_2 == 'none':
              valid_type2 = True
              type_2 = type_1
              valid = True
            elif valid_type_input(type_2):
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
            type_dict = dict['types']
            poke_type_list = []
            for items in type_dict:
                type = items['type']
                type_name = type['name']
                poke_type_list.append(str(type_name))

            poke_list.append([poke_id, poke_name, sprite, stats, poke_type_list])

    return poke_list


TYPES = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dark', 'dragon', 'steel', 'fairy']


##################### Figure creation, tidy up code later #####################

# def create_chart_from_pokemon(pokemon):

#     stats = pokemon[3]
#     x = []
#     y = []
#     name = pokemon[1]

#     if not os.path.exists('' + name + '.html'):
#       for items in stats:
#           x.append(items[0])
#           y.append(items[1])

#       colors = ['crimson', 'coral', 'moccasin', 'lightskyblue', 'lightgreen', 'lightpink']  

#       fig = go.Figure()
#       fig.add_trace(go.Bar(x=x, y=y, marker_color=colors))

#       # Add image
#       img = pokemon[2]
#       fig.add_layout_image(
#           dict(
#               source=img,
#               xref="paper", yref="paper",
#               x=1, y=1.05,
#               sizex=0.2, sizey=0.2,
#               xanchor="right", yanchor="bottom"
#           )
#       )


#       # Update layout
#       fig.update_yaxes(range=[0, 255])
#       fig.update_layout(title=(name))
#       fig.write_html('' + name + '.html') # export to HTML file


# Test 1: Empty list
# Test 2: Valid list
def generate_stat_table(pokemon):
    
    table_str = ""
    
    if pokemon:
      
      stats = pokemon[3]
      x = []
      y = []
      name = pokemon[1]
      table_str = name
      table_str = table_str + "\n -----------------------------"

      average = 0
      for items in stats:
          formatted_name = "{:<16}".format(items[0])
          table_str = table_str + "\n" + formatted_name + ' |  ' + str(items[1])
          average = average + items[1]

      average = (average / 6)
      table_str = table_str + "\n------------------------"
      formatted_avg = "{:<16}".format("average")
      table_str = table_str + "\n" + formatted_avg + ' |  ' + str(average)

    return table_str

def check_vulnerabilites(pokemon_team):
  
    #make a dict with all of the types, with the values being how much damage they do.
    matchups = {}
    for type in TYPES:
        matchups[type] = 1
    #iterate through team list.
    #for each poke in team, go through their 2 types and multiple dict key by their weaknesses.
      #if type_2 == type_1, don't do it

    for poke in pokemon_team:
        type_list = poke[2]
        type_1 = type_list[0]
        type_2 = type_list[1]

        # Go through types and calculate weaknesses.
        type_dict = json.load( open( type_1 + ".json" ) )
        double_damage_from = type_dict['double_damage_from']
        half_damage_from = type_dict['half_damage_from']

        for items in double_damage_from:
            matchups[items] = (matchups[items] * 2)
        for items in half_damage_from:
            matchups[items] = (matchups[items] * 0.5)

        if type_2 != type_1:
            type_dict = json.load( open( type_1 + ".json" ) )
            double_damage_from = type_dict['double_damage_from']
            half_damage_from = type_dict['half_damage_from']

            for items in double_damage_from:
                matchups[items] = (matchups[items] * 2)
            for items in half_damage_from:
                matchups[items] = (matchups[items] * 0.5)

    # for each really strong, go through team list and see if they have a pokemon that counters it.

    for type in matchups.items():
        counter = False
        if type[1] >= 2:
            # Check if team has a pokemon that counters the type.
            type_dict = json.load( open( type[0] + ".json" ) )
            double_damage_from = type_dict['double_damage_from']
            for item in double_damage_from:
                for poke in pokemon_team:
                    if (poke[2][0] == item) or (poke[2][1] == item):
                        counter = True

            if not counter:
                vulnerabilities = '/'.join(double_damage_from)
                print("Your team is weak to " + type[0] + " types. Consider adding a pokemon that is a " + vulnerabilities + " type.")

    # if they don't, then print 'you are weak to blah. considering adding a bleh type'
      
def ask_user_for_team():
  
    # Create database if it doesn't exist
    os.system('mysql-u root -pcodio-e "CREATE DATABASE IF NOT EXISTS '+ 'pokemon_teams' +'; "')
    load_database_from_file('poke_teams')
    engine = createEngine()
    insp = sqlalchemy.inspect(engine)

    pokemon_team = []
    num = 1
    # User is able to choose 6 pokemon.
    team_name = input("Enter your team name! ")

    while num <= 6:

        if num >= 4:
          check_vulnerabilites(pokemon_team)

        current_team_str = ''
        for poke in pokemon_team:
          current_team_str = current_team_str + ' | ' + str(poke[1])

        print("Current team -- " + current_team_str + '\n')

        num_display = '---------------- \n' + '|  Pokemon ' + str(num) + '   | \n---------------- \n'
        print(num_display)

        valid = False

        while not valid:
          user_team_input = get_team_inputs()

          t = get_by_type(user_team_input[0])
          t_list = get_pokes_from_json(t)

          t2 = get_by_type(user_team_input[1])
          t2_list = get_pokes_from_json(t2)

          combination = compare_poke_lists(t_list, t2_list)

          # If no pokemon have this type combination...
          if not combination:
              print("No pokemon have this type combination! Please try again. ")
          else:

              # show pokemon stats table and generate stats chart for user comparison
              # ask the user to choose a pokemon.
              # add chosen pokemon to list.
              print("Here is a list of results! Please choose which Pokemon you would like to add to your team. \n")
              pokes = get_pokemon_in_list(combination)
              pokemon_names = []
              poke_choices = []
              # Print out stats chart for each Pokemon
              for poke in pokes:
                  print(generate_stat_table(poke))
                  print('\n')
                  pokemon_names.append(str(poke[1]))
                  poke_choices.append( [str(poke[1]), poke[4]] )

              poke_chosen = False

              while not poke_chosen:
                  selected_poke = input("Enter the Pokemon you would like to select: ")
                  if selected_poke not in pokemon_names:
                      print("Name is not in list of available choices. Please try again.")
                  else:
                      index = pokemon_names.index(selected_poke)
                      pokemon_team.append([num, selected_poke, poke_choices[index][1]])
                      poke_chosen = True

              valid = True
              num = num + 1

    df = list_to_df(pokemon_team)
    create_database_table(df, team_name)
    save_database_to_file('poke_teams')
    print('Pokemon team completed! Please check the database to see your team.')

    return team_name
  
# t = get_by_type(user_input[0])
# t_list = get_pokes_from_json(t)

# t2 = get_by_type(user_input[1])
# t2_list = get_pokes_from_json(t2)

# combination = compare_poke_lists(t_list, t2_list)

# pokes = get_pokemon_in_list(combination)
# print(pokes)
  
#r = requests.get('https://pokeapi.co/api/v2/type/fire')
#dict = r.json()
#print(dict)



ask_user_for_team()
#print(get_by_type('').json())