'''
@author: root
'''
import os
import sys
from genieLibrary import commonVariables

class genieACSServer(object):
    '''
    classdocs
    '''
    serverIP = None
    serverPort = -1
    serverTimeout = -1
#    serverUserName = None
#    serverUserPassword = None
    localRoot = None

#    def __init__(self, serverIP : str = None, serverPort : int = None, serverUserName : str = None, serverUserPassword : str = None):
    def __init__(self, serverIP : str = None, serverPort : int = None, serverTimeout : int = None, localRoot : str = None) :
        '''
        Constructor
        '''
        if serverIP != None :
            self.serverIP = serverIP
        else :
            self.serverIP = commonVariables.DEFAULT_SERVERIP
        
        if type(serverPort) is int :
            self.serverPort = serverPort
        else :
            self.serverPort = commonVariables.DEFAULT_PORT

#        self.serverUserName = serverUserName
#        self.serverUserPassword = serverUserPassword
        if type(serverTimeout) is int and serverTimeout > 0 :
            self.serverTimeout = serverTimeout
        else :
            self.serverTimeout = commonVariables.DEFAULT_CONNECTION_TIMEOUT

        if type(localRoot) is str and os.path.isdir(localRoot) :
            self.localRoot = localRoot
        else :
            if sys.platform != 'win32' :
                self.localRoot = commonVariables.DEFAULT_ROOT_PATH_POSIX
            else :
                self.localRoot = commonVariables.DEFAULT_ROOT_PATH_WINDOWS
    
    def __del__(self):
        '''
        Destructor
        '''
        pass
    