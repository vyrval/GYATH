'''
Created on Jan 6, 2016

@author: T0157129
'''

class Item:
    '''
    This class represents any item of the game.
    '''


    def __init__(self, category, name, description, cost):
        '''
        Constructor
        '''
        self.category   =category
        self.name       =name
        self.description=description
        self.cost       =cost
        
    def __str__(self):
        return self.name