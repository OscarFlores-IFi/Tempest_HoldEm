#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Created on Fri May  1 18:38:03 2020

@author: of
"""

# Se simularan n escenarios, en los cuales se apuesta un 'all-in' para encontrar distribución adecuada para apostar el Tempest Hold'em.
# Falta incorporar imports relativos y sacar el documento de la carpeta.
# https://realpython.com/absolute-vs-relative-python-imports/
import time
from multiprocessing import pool, cpu_count

import numpy as np

from deck import Deck
from card import Card
from evaluator import Evaluator
from init_rank import init_rank

initial_ranking = init_rank.initial_ranking
evaluator = Evaluator()
thread_pool = pool.ThreadPool(cpu_count())

def juego(nplayers, pretty_print = False):
    deck = Deck()
    # Repartimos 2 cartas a cada jugador
    hands = [deck.draw(2) for _ in range(nplayers)]

    # Cada jugador decide si apuesta o no apuesta en base a su posici�n y su mano inicial.
    initial_rank = [initial_ranking(hand) for hand in hands] # ranking inicial p/2 jugadores, seg�n Michael Shackleford.

    # Se reparte las 5 cartas comunes.
    board = deck.draw(5)


    if pretty_print:
        [Card.print_pretty_cards(i) for i in hands] # imprime la mano de cada jugador
        Card.print_pretty_cards(board) # imprime tablero
        evaluator.hand_summary(board, hands) # imprime ganador

    # Se calcula el ranking de cadfloat64a mano.
    ranking = [evaluator.evaluate(hand, board) for hand in hands]
    return([initial_rank, ranking])

nplayers = 9
simulaciones = 10000

# No multiprocessing
# 9 jugadores, 10 simulaciones tardan 0.00508 seg.
# 9 jugadores, 100 simulaciones tardan 0.05172 seg.
# 9 jugadores, 1000 simulaciones tardan 0.45957 seg.
# 9 jugadores, 10000 simulaciones tardan 4.6288 seg.

t1 = time.time()
resultados = [juego(nplayers) for _ in range(simulaciones)]
print(time.time()- t1)

# multiprocessing
# 9 jugadores, 10 simulaciones tardan 0.01067 seg.
# 9 jugadores, 100 simulaciones tardan 0.06975 seg.
# 9 jugadores, 1000 simulaciones tardan 0.73980 seg.
# 9 jugadores, 10000 simulaciones tardan 7.5221 seg.
t1 = time.time()
resultados = thread_pool.map(juego, np.ones(simulaciones,dtype=int)*nplayers)
print(time.time()-t1)

print(resultados)
