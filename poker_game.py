#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:41:46 2019

@author: mayaaravapalli
"""
#importing random package 
import random 

#asking user to enter number of players 
print("Please enter number of players:")
number_of_players = int(input())

#creating a for loop to ask each player for their name 
for player in range(number_of_players): 
    names = [] 
    names.append(input("Please enter player name:"))
    
#creating the cards 

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4 

player_cards = [] 

for p in range(number_of_players): 
    cards_drawn = random.sample(cards, 5)
    player_cards.append(cards_drawn)

print(player_cards) 

#couldn't figure out the rest especially how to compare cards 
