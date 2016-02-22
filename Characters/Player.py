'''
Created on Jan 6, 2016

@author: T0157129
'''
from Characters.Character import MyCharacter



class Player(MyCharacter):
    '''
    This class represents the player.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        name = raw_input("Enter your name: ")
        MyCharacter.__init__(self, 100, name, 1)
    
    def __str__(self):
        string= """ -------------
                    Welcome %s, you are the chosen one. The one that will fight against all. 
                    Go ahead and defeat all creatures you can... 
                    HP: %s
                    Level: %s
                    Weapons: %s
                    Armor: %s
                    -------------""" \
                % (self.name, self.HP, self.lvl, self.equipment["weapon"], self.equipment["armor"])
        
        return string