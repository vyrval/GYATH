'''
Created on Feb 23, 2016

@author: T0157129
'''
from Characters.Character import MyCharacter


class Merchant(MyCharacter):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        MyCharacter.__init__(self, 100, "Marchand", 5)
        self.gold= 200
