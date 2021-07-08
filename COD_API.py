import requests
from bs4 import BeautifulSoup
import json
# 1. Connecting to COD the API 
# GET 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/' + username + '/profile/type/mp'

def get_by_username():
    username = input("Username: ")
    password = input("Password: ")
    final_token = ''
    csrf_token = requests.get('https://profile.callofduty.com/cod/login')
    csrf_parsed = BeautifulSoup(csrf_token.content, 'lxml')
    token = csrf_parsed.find_all("input")
    final_token = get_token(token)
    #print(token)
    data = {'username':  username, 
            'password':  password, 
            'remember_me': 'true', 
            '_csrf': final_token
           }
    files=[]
    headers = {
      'Cookie': 'XSRF-TOKEN='+ final_token   
    }
    print("code reaches here before post request")
    auth_response = requests.request("POST","https://profile.callofduty.com/do_login?new_SiteId=cod", headers=headers, data=data, files=files, verify=True, timeout=5)
    print(auth_response.status_code)
    print("code reaches here after post request")
    #{'status': 'error', 'data': {'type': 'com.activision.mt.common.stdtools.exceptions.NoStackTraceException', 'message': 'Not permitted: not authenticated'}}
    print(auth_response.status_code)
    #r = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/' + username + '/profile/type/mp', headers=auth_response)
    #File = r.json()
    #print(File)
    #print(File)
    #
def get_token(token):
    last_token =''
    for thing in token:
        if '_csrf' in str(thing):
            print(thing)
            x = (len(thing)-3)
            string_thing = str(thing)
            last_token = string_thing[41:x]
        else:
            break;
    return last_token
    # Get call for CSRF Token
    # Post call to login 
    # Get call for api

# 2. Storing whatever response in the appropriate data type: (array)
# 3. Setting up a MariaDB
# 4. Updating database with get request response
# 5. Integrating a pandas/matpllotlib funciton to display our information. information

#get_by_username() # %23
# username 'Lho%2311661'
#<input name="_csrf" type="hidden" value="YcXZRXkdfrHFX4oF_GS-8WtWWbzB5LNaYAmTeKHSf4tef1gv26XjpY1yE1sDt-nx"/>