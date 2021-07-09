import json
import pandas as pd
import sqlalchemy
import os
from sqlalchemy import create_engine

# Test 6: Result when dict has no items
# Test 7: Result when name is invalid
def create_database_table(df, name):
    engine = createEngine()
    df.to_sql(str(name), con=engine, if_exists='replace', index=False)
    print("Table created.")
    
def createEngine():
    engine = create_engine('mysql://root:codio@localhost/pokemon_teams')
    return engine


def save_database_to_file(file_name):
    os.system('mysqldump -u root -pcodio pokemon_teams > ' + file_name + '.sql')


def load_database_from_file(file_name):
    os.system('mysql -u root -pcodio pokemon_teams < ' + file_name + '.sql')


def list_to_df(list):
    formatted_list = []
    for item in list:
      formatted_list.append([item[0], item[1], item[2][0], item[2][1]])
    df = pd.DataFrame(formatted_list, columns=['id', 'pokemon', 'type_1', 'type_2'])
    return df