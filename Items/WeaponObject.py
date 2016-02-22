'''
Created on Jan 7, 2016

@author: T0157129
'''
from Items.Item import Item

class WeaponObject(Item):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        data["attackPoints"]= (int)(data.get("attackPoints"))
        Item.__init__(self, data)
        
    def __str__(self):
        string= "%s, %s, Attack: %s" % (self.name(), self.description(), str(self.attackPoints()))
        return string
    
    def attackPoints(self):
        return self.get("attackPoints")
    
    def getCopy(self):
        return WeaponObject(self.data)