'''
Created on Jan 14, 2016

@author: T0157129
'''


from Actions.Action import Action
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
        self.name       = XmlEvent.attributes["name"].value
        self.description= XmlEvent.attributes["description"].value
        self.text       = XmlEvent.attributes["text"].value
        
        #Parse Action/Next
        self.ActionsDict={}
        for XmlAction in XmlEvent.getElementsByTagName("Next"):
            action= Action(XmlAction, self.game)
            if Action is not None:
                self.ActionsDict[action.name]= action
        '''
        XmlAction= XmlEvent.children
        while XmlAction is not None:
            if XmlAction.type == "element":
                action= Action(XmlAction, self.game)
                if Action is not None:
                    self.ActionsDict[action.name]= action
            XmlAction= XmlAction.next
          '''
                
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
        valid = False
        while not valid:
            userAction = raw_input("What do you want to do? ")
            if self.ActionsDict.has_key(userAction):
                actionToDo = self.ActionsDict[userAction]
                if actionToDo is not None:
                    valid= True
                    next= actionToDo.doIt()
                    return next
        
    def __str__(self):
        return self.name
        