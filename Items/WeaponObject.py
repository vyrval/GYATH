'''
Created on Jan 7, 2016

@author: T0157129
'''
from Items.Item import Item

class WeaponObject(Item):
    '''
    classdocs
    '''


    def __init__(self, category, name, description, cost, attackPoints):
        '''
        Constructor
        '''
        Item.__init__(self, category, name, description, cost)
        self.attackPoints= attackPoints
        
    def __str__(self):
        string= "%s, %s, Attack: %s" % (self.name, self.description, str(self.attackPoints))
        return string