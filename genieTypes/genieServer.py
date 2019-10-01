'''
@author: root
'''
from genieLibrary import commonVariables

class genieACSServer(object):
    '''
    classdocs
    '''
    serverIP = None
    serverPort = -1
    serverUserName = None
    serverUserPassword = None

    def __init__(self, serverIP : str = None, serverPort : int = None, serverUserName : str = None, serverUserPassword : str = None):
        '''
        Constructor
        '''
        if serverIP != None :
            self.serverIP = serverIP
        else :
            self.serverIP = commonVariables.DEFAULT_SERVERIP
        
        if type(serverPort) is int and serverPort != None :
            self.serverPort = serverPort
        else :
            self.serverIP = commonVariables.DEFAULT_PORT

        self.serverUserName = serverUserName
        self.serverUserPassword = serverUserPassword
    
    