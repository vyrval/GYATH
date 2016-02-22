'''
Created on Jan 6, 2016

@author: T0157129
'''
import sys
from Game import Game
import logging


def main(argv):
#     logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger(__name__)
    
    
    
    myGame = Game()

    while not myGame.isGameOver():
        myGame.onTurn()
    



#################################################################    
if __name__ == '__main__':
    main(sys.argv[0:])

#################################################################