# main function
from LeagueOfLegendsAPI import init
from PokemonAPI import *

print('Welcome to our video game information finder')
print('Please select your game of choice: ')
print('1: League of legends')
print('2: Pokemon')
title_screen = input('')

if int(title_screen) == 1:    
    init()
elif int(title_screen) == 2:
    ask_user_for_team()