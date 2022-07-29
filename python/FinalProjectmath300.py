import itertools
import random
import math
import matplotlib.pyplot as TIRED


def Deck():
    deck = []
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')
    for c in itertools.product(SUITS,RANKS):
        deck.append(c)
    random.shuffle(deck)
    return deck



def Draw(deck):
    hand = []
    for i in range(5):
        hand.append(deck.pop())
    return hand

def straight(hand):
    if hand == ['Ace', '10', 'Jack', 'Queen', 'King']:
        return True
    else:
        return False

def Hand(hand):
    SUITS = []
    RANKS = []
    Values = {}
    for index in hand:
        SUITS.append(index[0])
    for index in hand:
        RANKS.append(index[1])
    RANKS.sort()
    
    for thesuit, theNumericalValue in hand:
        if theNumericalValue not in Values:
            Values[theNumericalValue] = 1
        else:
            Values[theNumericalValue] += 1
            
    if len(set(RANKS)) == 1:
        return "mwahhahahha"
        
            
    if len(set(RANKS)) == 2:
        for key in Values:
            if Values[key] == 4 or Values[key] == 1:
                return"Four of a kind"
            elif Values[key] == 3 or Values[key] == 2:
                return"Full house"
    
    if len(set(RANKS)) == 3:
        for key in Values:
            if Values[key] == 3 or Values[key] == 1:
                return"Three of a kind"
            elif Values[key] == 2 or Values[key] == 2:
                return"Two pair"
    
    if len(set(RANKS)) == 4:
        return"One pair"
        
    if len(set(RANKS)) == 5:
        if straight(Values):
            return "mehhhh"
        if not straight(Values):
            return "ehhhhh"
    

thedeck = Deck()
thehand = Draw(thedeck)
theresutls = Hand(thehand)

def multiple_results():
    return theresutls 
for _ in range(1000):
    print(multiple_results())

TIRED.scatter("thehand", "theresults")




