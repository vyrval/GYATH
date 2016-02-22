'''
Created on Jan 6, 2016

@author: T0157129
'''
import sys
from Game import Game
import logging


def main(argv):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    
    print("##################################################")
    print("                THE GAME BEGINS")
    print("##################################################")
    myGame = Game()

    while myGame.onGame():
        myGame.onTurn()
    
    print("##################################################")
    print("                 THE GAME ENDS")
    print("##################################################")


#################################################################    
if __name__ == '__main__':
    main(sys.argv[0:])

#################################################################