#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:22:57 2019

@author: mayaaravapalli
"""
#aaking the user for number of players playing the game 
print("please enter number of players:")
number_of_players = int(input()) 

#creating an empty list for adding all player names in the list 
names = [] 

#for loop for asking names of each player 
for player in range(number_of_players): 
    names.append(input("Please enter name of player {}:".format((number_of_players)))) 

#creating a list for suits and cards 
#importing random 
import random 

suit = ['c','d','h','s']
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

#create a deck of cards 

#from the deck of cards assign one to each player one at a time 
#pop the card that has already been used 


#work on 



