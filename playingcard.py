"""

LAB 5
Author: Ken Michna
Date: 5/26/2022
Description:
    Program randomly generates however many cards the user chooses

"""

import random

class PlayingCard:
    """A Class that defines a chosen playing card"""
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def get_value(self):    #Left out argument to see if I could
        """Returns the numerical value of the card"""
        rank = self.rank
        if rank == 1:
            value = 1
        elif rank > 1 and rank < 11:
            value = rank
        elif rank >= 11 and rank <=13:
            value = 10
        else:
            value = rank
            print("Invalid rank entered")
        return value
          
    def get_suit(self):
        """Returns the full name of the abbreviated suit"""
        suit = self.suit
        if suit == "d":
            suit = "Diamonds"
        elif suit == "s":
            suit = "Spades"
        elif suit == "c":
            suit = "Clubs"
        elif suit == "h":
            suit = "Hearts"
        else:
            print("Invalid suit entered")
        return suit
    
    def get_rank(self):
        """Returns the name of the card related to the rank"""
        rank = self.rank
        if rank == 1:
            card = "Ace"
        elif rank > 1 and rank < 11:
            card = str(rank)
        elif rank == 11:
            card = "Jack"
        elif rank == 12:
            card = "Queen"
        elif rank == 13:
            card = "King"
        else:
            card = rank
            print("Invalid rank entered")
        return card

    def __str__(self):
        return f"{self.get_rank()} of {self.get_suit()}"


#c = PlayingCard(11,"h")  tests for my later reference
#print(c.get_value())

suit_list = ["s","h","d","c"]    #List of suits for program to randomly choose from

generate = int(input("How many cards would you like to generate? "))

n = 0
while n <= generate:    #Generates as many random cards as the user chooses and displays their value
    rand_card = PlayingCard(random.randint(1,13),random.choice(suit_list))    #Chooses random number between 1-13 for arg 1 and a random suit from suit_list for arg 2
    print(f"{rand_card}: {rand_card.get_value()}")    #Prints card and associated value
    n += 1    #Advance n for while loop control