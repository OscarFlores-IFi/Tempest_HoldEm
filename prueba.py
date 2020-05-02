"""
Created on Fri May  1 18:38:03 2020

@author: of
"""

# Se simularan n escenarios, en los cuales se apuesta un 'all-in' para encontrar distribuciÃ³n adecuada para apostar el Tempest Hold'em.
# Falta incorporar imports relativos y sacar el documento de la carpeta. 
# https://realpython.com/absolute-vs-relative-python-imports/

from deck import Deck
from card import Card
from evaluator import Evaluator
import init_rank

evaluator = Evaluator()

# Repartimos 2 cartas a cada jugador

def juego(nplayers, pretty_print = False):
    deck = Deck()
    hands = [deck.draw(2) for _ in range(nplayers)]
    
    # Cada jugador decide si apuesta o no apuesta en base a su posición y su mano inicial.
    initial_rank = [init_rank.init_rank(hand) for hand in hands] # ranking inicial p/2 jugadores, según Michael Shackleford. 
    
    # Se reparte las 5 cartas comunes. 
    board = deck.draw(5)
    
    
    if pretty_print:
        [Card.print_pretty_cards(i) for i in hands] # imprime la mano de cada jugador
        Card.print_pretty_cards(board) # imprime tablero
        evaluator.hand_summary(board, hands) # imprime ganador
    
    # Se calcula el ranking de cada mano. 
    ranking = [evaluator.evaluate(hand) for hand in hands]
    return([initial_rank, ranking])
    #

nplayers = 9
juego(nplayers)
