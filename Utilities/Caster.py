'''
Created on Feb 24, 2016

@author: T0157129
'''


'''
    Cast a string into boolean.
    The trueVal list represents the accepted values for True.
    Return the boolean value.
'''
def strToBool(string):
    trueVal=['True', 'true', 't', '1']
    if string in trueVal:
        return True
    else:
        return False