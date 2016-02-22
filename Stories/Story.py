'''
Created on Jan 14, 2016

@author: T0157129
'''

from Stories.Event import Event
import xml.dom.minidom as minidom
import logging

class Story:
    '''
    classdocs
    '''


    def __init__(self, gameObj):
        logging.basicConfig(level=logging.DEBUG, disable_existing_loggers=False)        
        self.logger= logging.getLogger(__name__)
        '''
        Constructor
        '''        
        
        #Give ability to access to player, enemyGenerator etc...
        self.game= gameObj
        
        #Parse events in storyFile to eventDict
        self.eventDict= {}
        
        
        mfile = minidom.parse("./XML_Files/StoryFile.xml")
        events = mfile.getElementsByTagName("Event")
        for eventXml in events:
            event = Event(eventXml, self.game)
            self.eventDict[event.name]= event
        '''
        eventXml = root.children
        while eventXml is not None:
            if eventXml.type == "element":
                event = Event(eventXml, self.game)
                self.eventDict[event.name]= event
            eventXml= eventXml.next
       '''
    
        
    '''
    '''
    def goToEvent(self, eventName):
        next= self.eventDict[eventName].doIt()
        return next