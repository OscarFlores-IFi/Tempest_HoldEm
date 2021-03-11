# Tempest-HoldEm
Calculations of the 'optimal' actions taken by the players of a Tempest Hold'em game, variation of Texas Hold'em. 


El proyecto utiliza varios archivos tomados de https://github.com/msaindon/deuces.

Los documentos generados son:
Main.py
init_rank.py

El ranking de las manos se debe al trabajo del matemático Michael Shackleford, quien publicó la tabla de distribución de probabilidades para 2 jugadores con la mano inicial. Se paso manualmente los valores a un diccionario del cual se consultaran los datos para la toma de decisiones. Las manos se encuentran ordenadas de 1-169, siendo 1 la más fuerte (AA) y 169 la más debil (2,3, unsuited). La distribución considera si las manos originales tienen cartas del mismo palo (suited) o no (unsuited). 

El trabajo está documentado con más detalle en el Notebook de Jupyter. 


