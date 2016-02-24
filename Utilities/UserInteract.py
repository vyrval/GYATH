'''
Created on Feb 24, 2016

@author: T0157129
'''

'''
    Ask the user to enter a value contained in listAvailableActions.
    Stay stucked in while he doesn't.
    Return the user choice.
'''
def userIput(strToPrint, listAvailableActions):
    valid= False
    while not valid:
        useraction= raw_input(strToPrint)
        if useraction in listAvailableActions:
            valid=True
            return useraction

'''
    Ask the user to enter an integer value.
    Stay stucked in while he doesn't.
    Return the user value.
'''
def userInputInt(strToPrint):
    valid= False       
    while not valid:
        units= raw_input(strToPrint)
        try :
            units_val= int(units)
            valid= True
        except ValueError:
            print("It doesn't make sens...")
    return units_val