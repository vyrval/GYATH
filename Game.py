'''
Created on Jan 6, 2016

@author: T0157129
'''
import logging
import logging.config


from Characters.Player import Player
from Prefabs.WorldItems import WorldItems
from Prefabs.EnemyGenerator import EnemyGenerator
from Printer import Printer
from Stories.Story import Story

class Game:
    '''
    This class represents the whole game.
     
    '''


    def __init__(self):
        '''
        Constructor
        '''
#         logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)
#         self.logger = logging.getLogger(__name__)
        
        self.gameOver= False
        
        
        self.printer=Printer(self)
        
        self.WI= WorldItems()
        
        self.player = self.__initPlayer()
        
        
        # Enemies
        self.EG = EnemyGenerator(self.WI)
        
        self.currentEnemy= ""
        
        
        self.story = Story( self)
    
        self.printer.intro(self.player)
        self.player.listInventory()
        raw_input()
        
        self.nbTurn = 0
        
        print("##################################################")
        print("                THE GAME BEGINS")
        print("##################################################")
        
        self.nextEvent = self.story.goToEvent("intro")
        
        
    '''
    void onTurn()
    '''    
    def onTurn(self):
        self.nbTurn = self.nbTurn +1
        
        self.nextEvent = self.story.goToEvent(self.nextEvent)
                
        
        
    '''
    boolean onGame()
        Return true while the player isn't dead.
    '''       
    def onGame(self):
        return self.player.isAlive() and self.nbTurn<20
    
    
    def endGame(self):
        print("##################################################")
        print("                 THE GAME ENDS")
        print("##################################################")
        self.gameOver= True
        
    def isGameOver(self):
        return self.gameOver
    
    
    def __initPlayer(self):
        player = Player()
        player.equipArmor(self.WI.getArmorByCategory("basic"))
        player.equipWeapon(self.WI.getWeaponByCategory("basic"))
        potion = self.WI.getPotionByCategory("HP")
        potion.fill()
        player.addToBag(potion)
        return player