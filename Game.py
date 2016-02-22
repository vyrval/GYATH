'''
Created on Jan 6, 2016

@author: T0157129
'''
import logging
import logging.config


from Characters.Player import Player
from Prefabs.WorldItems import WorldItems
from Prefabs.EnemyGenerator import EnemyGenerator

class Game:
    '''
    This class represents the whole game.
     
    '''


    def __init__(self):
        '''
        Constructor
        '''
        logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
        
        
        self.WI= WorldItems()
        
        # Enemies
        self.EG = EnemyGenerator(self.WI)
        
        self.currentEnemy= self.EG.getEnemyByCategory("basic")
        
        self.player = Player()
        self.player.equipArmor(self.WI.getArmorByCategory("basic"))
        self.player.equipWeapon(self.WI.getWeaponByCategory("basic"))
        print(self.player)
        
        
        self.nbTurn = 0
        
        
        print("")
        print("Your current ennemy is: %s" % self.currentEnemy)
        
    
    '''
    void onTurn()
        A turn is:
            # Create a mob
            # FIGHT
            #    player attacks
            #    mob attacks
            # Reward
    '''    
    def onTurn(self):
        self.nbTurn = self.nbTurn +1
        
        print("--------------------------------------------------")
        print("Turn %d begins...." % self.nbTurn)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")

        self.player.attack(self.currentEnemy)
        self.currentEnemy.attack(self.player)
        
        print("Player HP: %d." % self.player.HP)
        print("Enemy  HP: %d." % self.currentEnemy.HP)
        #self.player.onTurn()
        
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("Turn %d ends...." % self.nbTurn) 
        print("--------------------------------------------------") 
        raw_input()
        
    '''
    boolean onGame()
        Return true while the player isn't dead.
    '''       
    def onGame(self):
        return self.player.isAlive() and self.nbTurn<2