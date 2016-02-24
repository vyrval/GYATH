'''
Created on Jan 6, 2016

@author: T0157129
'''

import copy


class Item:
    '''
    This class represents any item of the game.
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.data= data
        
        
    def __str__(self):
        return self.name
    
    
    def category(self):
        return self.data.get("category")
    
    def name(self):
        return self.data.get("name")
    
    def description(self):
        return self.data.get("description")
    
    def cost(self):
        return self.data.get("cost")


    def get(self, name):
        return self.data.get(name)
    def set(self, name, value):
        self.data[name]= value