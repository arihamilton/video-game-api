import requests
import json
# 1. Connecting to League the API 
# GET 'https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/' + username + '/profile/type/mp'
def get_by_username(username):
    r = requests.get('https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/' + username + '/profile/type/mp')
    File = r.json()
    print(File)
    # Get call for CSRF Token
    # Post call to login 
    # Get call for api
# 2. Storing whatever response in the appropriate data type: (array)
# 3. Setting up a MariaDB
# 4. Updating database with get request response
# 5. Integrating a pandas/matpllotlib funciton to display our information. information

get_by_username('Lho%2311661') # %23

