# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:43:00 2021

@author: OF

Millionaire game. 
A game with an easy dynamic. there are given 2 cards
you have to bet at least $1.
if the following card (a third one) fits between the 2 previous cards,
then you earn the amount you have bet. if not, you lose the bet. 
"""
import numpy as np


def win_lose(cards):
    card1 = cards[0:2].min()
    card2 = cards[0:2].max()
    card3 = cards[2]
    dif = card2-card1-1 # Amount of cards whithin card 1 and 2
    result = 1 if card3 < card2 and card3 > card1 else -1 # if third card fits between 1 and 2 its a win, else its a loss. 
    return [dif, result] # 0 if we lose, 1 if we win

def game():
    Deck = np.concatenate((np.arange(13),np.arange(13),np.arange(13),np.arange(13)))   # We start by setting a Deck
    cards = np.random.choice(Deck,3)     # We deliver the 3 cards (we would bet before we knew the third one)
    # return  win_lose(np.random.choice(Deck,3))
    return  win_lose(cards)
    

initial_amount = 100

print([game() for _ in range(50)])