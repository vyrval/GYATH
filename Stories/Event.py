'''
Created on Jan 14, 2016

@author: T0157129
'''


from Actions.Action import Action
from Utilities import UserInteract as ui


import xml.dom.minidom as minidom
import logging

class Event:
    '''
    classdocs
    '''


    def __init__(self, XmlEvent, gameObj):
        '''
        Constructor
        '''
        self.logger= logging.getLogger(__name__)
        
                
        self.ActionsDict={}
        self.game= gameObj
        
        

        #Parse properties
        self.name       = (str)(XmlEvent.attributes["name"].value)
        self.description= (str)(XmlEvent.attributes["description"].value)
        self.text       = (str)(XmlEvent.attributes["text"].value)
        
        #Parse Action/Next
        self.ActionsDict={}
        for XmlAction in XmlEvent.getElementsByTagName("Next"):
            action= Action(XmlAction, self.game)
            if action is not None:
                self.ActionsDict[action.name()]= action


    def doIt(self):
        
        #Print the text of the event
        print(". . . . . . . . . . . . . . . .")
        print(self.text)
        
        #Print the possible actions
        string= "Available actions: "

        for action in self.ActionsDict.keys():
            if action =="die":
                self.game.endGame()
                return action
            string= string + " " + action
        print(string)
        
        #Parse the user input
        userAction= ui.userIput("What do you want to do? ", self.ActionsDict.keys())
        actionToDo= self.ActionsDict[userAction]
        return actionToDo.doIt()
    
        
    def __str__(self):
        return self.name
        