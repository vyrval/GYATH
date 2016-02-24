'''
Created on Jan 14, 2016

@author: T0157129
'''


from Utilities.Switch import switch
from Utilities import XmlParser as xmlp


import logging

class Action:
    '''
    classdocs
    '''


    def __init__(self, XmlAction, gameObj):
        self.logger= logging.getLogger(__name__)
        '''
        Constructor
        '''
        
        self.game= gameObj

        #Parse properties
        self.data= xmlp.parseAttributes(XmlAction)


    
    def doIt(self):
        player = self.game.player
        
        for case in switch(self.name()):
            if case('fight'):
                enemy= self.game.EG.getEnemyByName(self.get('enemy'))
                while player.isAlive() and enemy.isAlive() :
                    print("# # # # # # # # # # # # # # # #")
                    self.game.printer.character(player)
                    self.game.printer.character(enemy)
                    print("- - - - - - - - - - - - - - - -")
                    
                    player.fight(enemy)
                    if enemy.isAlive():
                        enemy.attack(player)
                    else: 
                        print("You've defeated the %s!!!" % enemy.name)
                        player.gainExp(enemy.expPoints)
                        reward=self.get('reward') 
                        if reward is not None:
                            objReward= self.game.WI.get(reward)
                            player.loot(objReward)
                    print("# # # # # # # # # # # # # # # #")
                    raw_input()
                    
                enemy= None
                
                if player.isAlive():
                    return self.next()
                else:
                    self.game.endGame()
                    return "die"
                break
            
            if case('die'):
                return None
                break
            
            if case(): # default, could also just omit condition or 'if True'
                reward=self.get('reward') 
                if reward is not None:
                    objReward= self.game.WI.get(reward)
                    player.loot(objReward)
                return self.next()
                # No need to break here, it'll stop anyway
    
    
    def name(self):
        return self.get("action")
    def next(self):
        return self.get("next")
    
    
    def get(self, name):
        return self.data.get(name)
    def set(self, name, val):
        self.data[name]=val
    
    
    def __str__(self):
        return self.name()