import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
# Connect to the League API
# Obtain information with a get requests
# Place information into JSON file
# Database that jawn 
# Graphs and shit

def init():
    # get summoner region and name via input
    # Maybe add a function to parse the response and ensure a correct region is collected
    summoner_name = input("League Summoner Name: ")
    #summoner_name = "LH0"
    #summoner_region = "na1"
    summoner_region = input("Your Region: ")
    api_key = 'RGAPI-4842d23e-2258-4b89-b112-9e5fcb41a024'
    get_request_response = initial_get_request(summoner_name,summoner_region,api_key)
    summoner_id = get_summoner_id(get_request_response)
    graph(champion_mastery(summoner_name,summoner_region,summoner_id,api_key))
    
    
def initial_get_request(_name,_region,_api):
    url = "https://"+_region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+_name+"?api_key="+_api

    response = requests.request("GET", url)
    return response
    
def get_summoner_id(response):
  
    File = response.json()
    encrypted_summoner_id = File['id']
    summoner_puuid = File['puuid']
    return encrypted_summoner_id
  
def get_summoner_puuid(response):
  
    File = response.json()
    summoner_puuid = File['puuid']
    
    return summoner_puuid
    
    
def champion_mastery(_name,_region,encrypted_summoner_id,_api):
  
    url = "https://"+_region+".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+ encrypted_summoner_id+"?api_key="+_api 
    response = requests.request("GET", url)
    return graph_champion_mastery(response)
  
def graph_champion_mastery(response):
  
    File = response.json()
    # add a name column to our File
    New_File = name_column(File)
    data_frame = pd.DataFrame(New_File)
    # no need for the summonerid in our file
    data_frame = data_frame.drop(['summonerId'], axis=1)
    
    return data_frame
        
def graph(_frame_):
  
    plot = _frame_.iloc[0:10].plot.bar(x="ChampionName", 
                                       y=["championPointsSinceLastLevel","championPoints","championLevel"],
                                       subplots=True,figsize=(15,10))
    #_frame_.plot.line(y="tokensEarned")
  
# A small problem I've noticed is that the original data set from riot games doesn't name the champions. Instead it only provides id's
# Below is a function to convert champion add a column for champion names given ids to my data_frame
def name_column(_data_):
    # the source for my name json file
    url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
    champion_list = requests.request("GET", url)
    File = champion_list.json()
    _data_frame = File.pop('data')
    names_list=[]
    for key,value in _data_frame.items():
        temp_dict = {}
        element = _data_frame[key]
        temp_dict['name'] = element['id'] 
        temp_dict['id'] = element['key'] 
        names_list.append(temp_dict)
    
    for thing in _data_:
        for things in names_list:
              if int(thing['championId']) == int(things['id']):
                    thing['ChampionName'] = str(things['name'])
    return _data_                 

    
init()
plt.show()
