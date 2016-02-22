'''
Created on Jan 6, 2016

@author: T0157129
'''
from Characters.Character import MyCharacter
from Utilities.Switch import switch


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
        
        self.exp = self.exp-self.expMax
        self.level = self.level + 1
        self.HPinit = self.HPinit + gainHP
        self.HP = self.HP + gainHP
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
        valid = False
        while not valid:
            userAction = raw_input("What do you want to do? ")
            if userAction in actions:
                actionToDo={}
                actionToDo["action"]=userAction
                actionToDo["enemy"] =EnemyObj
                valid= True
                self.__parseUserAction(actionToDo)
    
    def __parseUserAction(self, action):
        
        for case in switch(action["action"]):
            if case('attack'):
                self.attack(action["enemy"])
                break
            if case('heal'):
                self.useFromBag("HP_potion")
                break
            
            
        
        
        

        