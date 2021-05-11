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
import pandas as pd
import matplotlib.pyplot as plt

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
    

# initial_amount = 100
n_sim = 1000

sims = np.array([game() for _ in range(n_sim)])
df_sims = pd.DataFrame(sims)

print('Only convenient to bet when expected value is bigger than 0')
print(df_sims.groupby(0).mean())
plt.plot(df_sims.groupby(0).mean()) # best fit: y = 0.15x-1
plt.hlines(0, -1, 11)


print('Probabilities of getting every difference: ')
print(df_sims.iloc[:,0].value_counts())
df_sims.iloc[:,0].value_counts().plot(kind='bar')



difs = df_sims.iloc[:,0]
print('You should bet : {} times out of {} times'.format(difs[difs >= 7].count(),n_sim))
print('You should not bet : {} times out of {} times'.format(difs[difs < 7].count(),n_sim))

ress = df_sims.iloc[:,1]
print('Expect to win {} times each of the bets'.format(ress[difs>=7].mean()))
