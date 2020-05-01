# Se simularan n escenarios, en los cuales se apuesta un 'all-in' para encontrar distribuciÃ³n adecuada para apostar el Tempest Hold'em.
# Falta incorporar imports relativos y sacar el documento de la carpeta. 
# https://realpython.com/absolute-vs-relative-python-imports/


from deck import Deck
from card import Card
from evaluator import Evaluator
import init_rank



deck = Deck()
evaluator = Evaluator()


# Repartimos 2 cartas a cada jugador
nplayers = 9
def juego(nplayers, pretty_print = False):
    hands = [deck.draw(2) for _ in range(nplayers)]
    
    # Cada jugador decide si apuesta o no apuesta en base a su posición y su mano inicial.
    init_rank = [initial_ranking(hand) for hand in hands] # ranking inicial p/2 jugadores, según Michael Shackleford. 
    
    # Se muestran las 5 cartas del piso. 
    board = deck.draw(5)
    
    
    if pretty_print:
        [Card.print_pretty_cards(i) for i in hands]
        Card.print_pretty_cards(board)
        evaluator.hand_summary(board, hands)
    
    
    
    # Se calcula quien fue el ganador. 
    
