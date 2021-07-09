import unittest
from LeagueOfLegendsAPI import *

class LOL_Unittest(unittest.TestCase):
    def test_initial_get_request(self):
        self.assertIsNotNone(initial_get_request('LH0','na1',api_key), msg = "None")
    def test_get_summoner_id(self):
        test_get_response = initial_get_request('LH0','na1',api_key)
        test_summoner_id = get_summoner_id(test_get_response)
        self.assertIsNotNone(get_summoner_id(test_get_response), msg = "None")
    def test_get_summoner_puuid(self):
        test_get_response = initial_get_request('LH0','na1',api_key)
        test_summoner_id = get_summoner_id(test_get_response)
        self.assertIsNotNone(get_summoner_puuid(test_get_response), msg = "None")
    def test_champion_mastery(self):
        test_get_response = initial_get_request('LH0','na1',api_key)
        test_summoner_id = get_summoner_id(test_get_response)
        self.assertIsNotNone(champion_mastery('LH0','na1',str(test_summoner_id),api_key))
        
if __name__ == '__main__':
    unittest.main()