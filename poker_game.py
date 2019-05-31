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

#######alternative way I tried doing it#################

import random


#asking the user for number of players
print("Please enter number of players: ")
number_of_players = int(input())

#creating a function to run the game:

def game(number_of_players):
    #asking the user to enter the name of each of the players
    for p in range(number_of_players):
        names = []
        names.append(input("Please enter name of players: "))
    #creating the cards (multipled by 4 for each of the suits)
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a'] * 4
    card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    #the card values above will be used to compare cards and determine the winner in the end

    #create a dictionarory of the cards held by each player
    #end goal for the next few lines of code is to successfully assign 5 cards to each player and linking
    #them with the names of each of the players
    players_and_cards= { } #empty dictionary where the
    assigning_cards_list= {} #this is the dictionary that will be used when comaring the hands in order to determine the winner

    #not entirely sure if i'm doing this right lol

    #creating a for loop to assign each of the elements in names to recieve 5 random cards
    for n in names:
        players_and_cards[n] = [] #this line of code creates a list with each of the players names
        assigning_cards_list[n] = []
        for num in range(0,5):#this is the start of starting the random drawing
            random_card = random.sample(cards, 5)
            cards.remove(random.sample)
            
