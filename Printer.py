'''
Created on Jan 11, 2016

@author: T0157129
'''

class Printer:
    '''
    classdocs
    '''


    def __init__(self, Game):
        '''
        Constructor
        '''
        self.game= Game
        
    def character(self, character):
        mstring="""    -------------------
    |Name: %s
    |HP: %d/%d
    |Lvl: %d
    |Weapon: %s
    |Armor: %s
    -------------------""" % (character.name,\
       character.HP, character.HPinit, \
       character.level, \
       self.__weaponOfChar(character), self.__armorOfChar(character))
        print( mstring)
    
    
    def __armorOfChar(self, character):
        return self.__armor(character.equipment["armor"])
    def __weaponOfChar(self, character):
        return self.__weapon(character.equipment["weapon"])
    
    def __armor(self, armor):
        mstring=""
        if armor is not None:
            mstring="""%s, %s
            Defense: %d""" \
            %(armor.name(), armor.description(), armor.defensePoints())
        return mstring  
    
    def __weapon(self, weapon):
        mstring=""
        if weapon is not None:
            mstring="""%s, %s
            Attack: %d""" \
            %(weapon.name(), weapon.description(), weapon.attackPoints())
        return mstring  
    
    
    def intro(self, character):
        mstring= """
*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
Welcome %s, you are the chosen one. The one that will fight against all. 
Go ahead and defeat all creatures you can... 
HP: %s
Level: %s
Weapons: %s
Armor: %s
- - - - - - - - - - - - -
""" % (character.name, character.HP, character.level, self.__weaponOfChar(character), self.__armorOfChar(character))
        print(mstring)