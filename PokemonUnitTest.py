import unittest
from PokemonAPI import *


class PokemonUnitTest(unittest.TestCase):


    def test_get_type(self):
        # Invalid input
        self.assertEqual(get_by_type('flame'), -1)
        # Uppercase input -- valid
        self.assertNotEqual(get_by_type('FIRE'), -1)
        # Standard valid input
        self.assertNotEqual(get_by_type('fire'), -1)
        # Empty input -- invalid
        self.assertEqual(get_by_type(''), -1)


    def test_get_pokes_from_json(self):
        type_request = get_by_type('fire')
        # Valid input
        self.assertTrue(len(get_pokes_from_json(type_request)) > 0)
        # Invalid input
        self.assertEqual(get_pokes_from_json('dfsf'), [])
        
        empty = {}
        # Empty input
        self.assertEqual(get_pokes_from_json(empty), [])


    def test_compare_poke_lists(self):
        # Valid input - ice/water pokemon exist
        ice = get_pokes_from_json(get_by_type('ice'))
        water = get_pokes_from_json(get_by_type('water'))
        self.assertTrue(len(compare_poke_lists(ice, water)) > 0)

        poison = get_pokes_from_json(get_by_type('poison'))
        # Valid input, empty output - Ice/Poison pokemon do not exist
        self.assertEqual(compare_poke_lists(ice, poison), [])
        
        # Empty inputs
        self.assertEqual(compare_poke_lists([],[]), [])
        
        # Empty & Non Empty input
        self.assertEqual(compare_poke_lists(ice, []), [])


    def test_valid_type(self):
        # Invalid input
        self.assertEqual(valid_type_input('flame'), False)
        # Lowercase input -- valid
        self.assertEqual(valid_type_input('fire'), True)
        # Uppercase input -- valid
        self.assertEqual(valid_type_input('FIRE'), True)
        # Empty input -- invalid
        self.assertEqual(valid_type_input(''), False)


    def test_generate_suggestion(self):
      
        TYPES = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dark', 'dragon', 'steel', 'fairy']
      
        # No suggestion generated
        self.assertEqual(generate_suggestion('flame', TYPES), -1)
        # No suggestion generated -- empty
        self.assertEqual(generate_suggestion('', TYPES), -1)
        # Suggestion generated
        self.assertEqual(generate_suggestion('fly', TYPES), "flying")
        # Suggestion generated
        self.assertEqual(generate_suggestion('fight', TYPES), "fighting")


    def test_get_team_inputs(self):
        # Valid input
        self.assertEqual(get_team_inputs(), ['fire', 'flying'])


    def test_get_pokemon_in_list(self):
        # Empty input
        self.assertEqual(get_pokemon_in_list([]), [])
        
        t = get_by_type('ice')
        poke_list = get_pokes_from_json(t)
        # Valid input
        self.assertNotEqual(get_pokemon_in_list(poke_list), [])


    def test_stat_table(self):
        # Empty input
        self.assertEqual(generate_stat_table([]), "")
        
        t = get_by_type('fairy')
        poke_list = get_pokes_from_json(t)
        real_poke_list = get_pokemon_in_list(poke_list)
        # Valid input
        self.assertNotEqual(generate_stat_table(real_poke_list[0]), "")


    def test_vulnerabilities(self):
        # Empty input
        self.assertNotEqual(check_vulnerabilites([]), "")


    def test_ask_user(self):
        # Valid input
        self.assertEqual(ask_user_for_team(), 'team')


if __name__ == '__main__':
    unittest.main()