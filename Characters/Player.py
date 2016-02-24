'''
Created on Jan 6, 2016

@author: T0157129
'''
from Characters.Character import MyCharacter
from Utilities.Switch import switch
from Utilities import UserInteract as ui

from Items.ArmorObject import ArmorObject
from Items.Item import Item
from Items.PotionObject import PotionObject
from Items.WeaponObject import WeaponObject


class Player(MyCharacter):
    '''
    This class represents the player.
    '''


    def __init__(self, HP):
        '''
        Constructor
        '''
        HP_player= 100
        if HP is not None:
            HP_player= (int)(HP)
            
        name = raw_input("Enter your name: ")
        MyCharacter.__init__(self, HP_player, name, 1)
        
        self.exp= 0
        self.expMax= 100
        
        
    
    def __str__(self):
        string= """ -------------
                    Welcome %s, you are the chosen one. The one that will fight against all. 
                    Go ahead and defeat all creatures you can... 
                    HP: %s
                    Level: %s
                    Weapons: %s
                    Armor: %s
                    -------------""" \
                % (self.name, self.HP, self.level, self.equipment["weapon"], self.equipment["armor"])
        
        return string
    
    
    def gainExp(self, XpPoints):
        self.exp = self.exp + XpPoints
        print("%s gained %d XP." % (self.name, XpPoints))
        if self.exp > self.expMax:
            self.__lvlup()
        
            
            
    def __lvlup(self):
        gainHP = 20
        
        self.exp    = self.exp-self.expMax
        self.level  = self.level + 1
        self.HPinit = self.HPinit + gainHP
        self.HP     = self.HP + gainHP
        print("%s has just reached level %d." % (self.name, self.level))
        
        
        
    def fight(self, EnemyObj):
        string = "Available actions: "
        actions=[]
        actions.append("heal")
        actions.append("attack")
        for act in actions:
            string = string + act +" "
        print(string)
        
        #Parse the user input
        userAction =ui.userIput("What do you want to do? ", actions)
        actionToDo={}
        actionToDo["action"]=userAction
        actionToDo["enemy"] =EnemyObj
        self.__parseUserAction(actionToDo)
    
    def __parseUserAction(self, action):
        
        for case in switch(action["action"]):
            if case('attack'):
                self.attack(action["enemy"])
                break
            if case('heal'):
                self.useFromBag("HP_potion")
                break
            
            
        
        
    def loot(self, reward):
        if reward is not None:
            print("You've found %s." % (reward))
            availableAct=[]
            availableAct.append('discard')
            availableAct.append('put_in_bag')
            
            if isinstance(reward, ArmorObject):
                print("You're equipped with %s" % (self.equipment["armor"]))
                availableAct.append('equip')
            
            elif isinstance(reward, WeaponObject):
                print("You're equipped with %s" % (self.equipment["weapon"]))
                availableAct.append('equip')

            elif isinstance(reward, Item):
                pass
            
            elif isinstance(reward, PotionObject):
                if reward.category() == 'HP':
                    availableAct.remove('put_in_bag')
                    potion= self.bag.get('HP_potion')
                    if potion is not None:
                        print("Your have %d/%d HP." %(self.HP, self.HPinit))
                        print("Your HP potion contains %d/%d units." % (potion.get('content'), potion.get('contentMax')))
                        availableAct.append('fill')
                        availableAct.appenf('use')
            
            string= "Available actions: "
            for act in availableAct:
                string= string + ' ' + act
            print(string)
            
            useraction= ui.userIput("What do you want to do? ", availableAct)
            self.__parseActions(useraction, reward)
            
            
    def __parseActions(self, userAction, reward):
        for case in switch(userAction):
            if case('discard'):
                break
            
            if case('put_in_bag'):
                self.addToBag(reward)
                break
            
            if case('equip'):
                if isinstance(reward, WeaponObject):
                    self.equipWeapon(reward)
                if isinstance(reward, ArmorObject):
                    self.equipArmor(reward)
                break
            
            if case('fill'):
                if isinstance(reward, PotionObject):
                    if reward.category() == "HP":
                        potion= self.bag.get("HP_potion")
                        if potion is not None:
                            potion.fill()
                break
            
            if case('use'):
                reward.use(self)
                break
            
               
            